import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from lumofy_lms.courses.models import Course
from lumofy_lms.courses.models import Enrollment
from lumofy_lms.courses.models import Lesson
from lumofy_lms.users.tests.factories import UserFactory

from .factories import CourseFactory
from .factories import EnrollmentFactory
from .factories import LessonFactory
from .factories import StudentFactory
from .factories import TeacherFactory

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="12345")  # noqa: S106


@pytest.fixture
def admin_user(db):
    return UserFactory(is_staff=True)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course(db):
    teacher = TeacherFactory()
    return CourseFactory(teacher=teacher)


@pytest.fixture
def lessons(db, course):
    return LessonFactory.create_batch(3, course=course)


@pytest.fixture
def student(db):
    return StudentFactory()


@pytest.fixture
def enrollment(db, course, student):
    return EnrollmentFactory(course=course, student=student)


@pytest.mark.django_db
def test_course_list_create(api_client, admin_user, course):
    url = "/courses/"
    api_client.force_authenticate(user=admin_user)
    response = api_client.get("/courses/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

    teacher = TeacherFactory()
    data = {
        "name": "Calculus 101",
        "description": "Introduction to Calculus",
        "teacher": teacher.id,
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.filter(name="Calculus 101").exists()


@pytest.mark.django_db
def test_course_retrieve_update_delete(api_client, admin_user, course):
    url = f"/courses/{course.id}/"
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == course.name
    updated_data = {"name": "Algebra 102", "description": "Advanced Algebra"}
    response = api_client.patch(url, updated_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert Course.objects.get(id=course.id).name == "Algebra 102"
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Course.objects.filter(id=course.id).exists()


@pytest.mark.django_db
def test_course_progress(api_client, admin_user, course):
    url = f"/courses/{course.id}/"
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0


@pytest.mark.django_db
def test_lesson_list(api_client, admin_user, lessons):
    url = "/courses/lessons/"
    api_client.force_authenticate(user=admin_user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
