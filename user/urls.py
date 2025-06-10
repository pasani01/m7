from django.urls import path
from .views import (
    RegisterView,
    ChangePasswordView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    ShowUserView,
    UserProfileUpdateView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('show-user/', ShowUserView.as_view(), name='show-user'),
    path('update-profile/', UserProfileUpdateView.as_view(), name='update-profile'),
    path('password-reset/request/', PasswordResetRequestView.as_view()),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view()),
]
