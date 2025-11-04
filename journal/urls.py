from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from.views import JournalDetailAPIView
from.views import JournalUpdateAPIView 
from .views import JournalCreateAPIView
from .views import JournalDestroyAPIView
from .views import UserRegisterAPIView
from .views import UserListAPIView
from .views import UserRetrieveUpdateAPIView


urlpatterns = [
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Journal endpoints
    path('journals/<int:pk>/', JournalDetailAPIView.as_view(), name='journal-detail'),
    path('journals/<int:pk>/update/', JournalUpdateAPIView.as_view(), name='journal-update'),
    path('journals/', JournalCreateAPIView.as_view(), name='journal-create'),
    path('journals/<int:pk>/delete/', JournalDestroyAPIView.as_view(), name='journal-delete'),

    # User endpoints
    path('users/register/', UserRegisterAPIView.as_view(), name='user-create'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/me/', UserRetrieveUpdateAPIView.as_view(), name='user-profile'),
]



