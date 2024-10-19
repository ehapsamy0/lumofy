from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import views

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from lumofy_lms.users.serializers import UserRegisterationSerializer
from lumofy_lms.users.serializers import UserSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class UserDetails(views.APIView):
    def get(self, request, format=None):
        """
        Return a User Data.
        """
        return Response(
            UserSerializer(instance=request.user).data, status=status.HTTP_200_OK
        )

