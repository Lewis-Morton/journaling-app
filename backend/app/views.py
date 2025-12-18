from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from.models import JournalEntry, User
from.serializers import JournalEntrySerializer, UserSerializer, RegisterSerializer
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit



# Create your views here.

# Views for journalentry model

# These views handle CRUD operations on journal entries

# Custom permission to ensure users can only access their own journals
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class JournalListAPIView(generics.ListAPIView):
    serializer_class = JournalEntrySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # Return only journals belonging to authenticated user and list in order created by
    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-created_at')

class JournalCreateAPIView(generics.CreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # Set the user to the authenticated user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JournalDetailAPIView(generics.RetrieveAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    # Return only journals belonging to the authenticated user
    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

class JournalUpdateAPIView(generics.UpdateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

class JournalDestroyAPIView(generics.DestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

# User Views

# Registers new user

# Registers new users
@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class UserRegisterAPIView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# List all users (admin -only)
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

# Retieves and updates user profile (self-only)
class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

