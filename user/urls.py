from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

app_name = 'user'

urlpatterns = [
    path("api/user/register/", registerUser, name="user-register"),
    path('api/user/login/', LoginUser.as_view(), name='token_obtain_pair'),
    path("api/user/profile/", getUserProfile, name="user-profile"),
]