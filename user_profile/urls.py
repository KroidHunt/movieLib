from django.urls import path

from user_profile.views import UserProfileView, CreateUserProfile, CreateSuperUserProfile

urlpatterns = [
    path('new/', CreateUserProfile.as_view(), name="newUserProfile"),
    path('super/new/', CreateSuperUserProfile.as_view(),
         name="newSuperUserProfile"),
    path('me/', UserProfileView.as_view(), name="getUserProfile")
]
