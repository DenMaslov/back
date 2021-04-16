from django.urls import path
from .views import CustomUserCreate, UserProfile

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('profile/', UserProfile.as_view(), name="get_user_profile"),
]
