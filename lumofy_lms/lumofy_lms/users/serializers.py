from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Student
from .models import Teacher

User = get_user_model()


class UserRegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(UserRegisterationSerializer):
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "role"]  # noqa: F811

    def get_role(self, instance):
        return "Admin" if instance.is_staff else "User"


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"  # noqa: F811



class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"  # noqa: F811

