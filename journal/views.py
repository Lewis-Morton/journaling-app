from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from.models import JournalEntry
from.models import User
from.serializers import JournalEntrySerializer
from.serializers import UserSerializer
from.serializers import RegisterSerializer
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit



# Create your views here.

# Views for journalentry model

# These views handle CRUD operations on journal entries
@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class JournalCreateAPIView(generics.CreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalDetailAPIView(generics.RetrieveAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalUpdateAPIView(generics.UpdateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalDestroyAPIView(generics.DestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

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
    permission_classes = [permissions.IsAdminUser]

# Retieves and updates user profile (self-only)
class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

