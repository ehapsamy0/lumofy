import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from .factories import StudentFactory
from .factories import TeacherFactory
from .factories import UserFactory

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="12345")  # noqa: S106


@pytest.fixture
def teacher(db):
    return TeacherFactory()


@pytest.fixture
def student(db):
    return StudentFactory()


@pytest.mark.django_db
def test_obtain_token(user):
    client = APIClient()
    response = client.post(
        "/users/login/", {"username": "testuser", "password": "12345"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_obtain_failed_token(user):
    client = APIClient()
    response = client.post(
        "/users/login/", {"username": "testuser000", "password": "12345"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "message" in response.data






@pytest.mark.django_db
def test_user_details_unauthenticated():
    client = APIClient()
    response = client.get("/users/user/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_user_details_authenticated(user):
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get("/users/user/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == user.username
    assert "email" in response.data
