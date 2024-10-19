import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .factories import TeacherFactory
from .factories import StudentFactory
from .factories import UserFactory

User = get_user_model()



@pytest.fixture()
def teacher(db):
    return TeacherFactory()


@pytest.fixture()
def student(db):
    return StudentFactory()


