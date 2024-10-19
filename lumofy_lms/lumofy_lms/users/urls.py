from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from lumofy_lms.users.views import MyTokenObtainPairView
from lumofy_lms.users.views import UserDetails

app_name = "users"
urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", UserDetails.as_view(), name="user"),
]
