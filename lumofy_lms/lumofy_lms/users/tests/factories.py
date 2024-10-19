import factory
from django.utils import timezone
from factory import Faker
from factory import LazyAttribute
from factory import post_generation
from factory.django import DjangoModelFactory

from lumofy_lms.courses.models import Course
from lumofy_lms.courses.models import Enrollment
from lumofy_lms.courses.models import Lesson
from lumofy_lms.courses.models import LessonCompletion
from lumofy_lms.users.models import Student
from lumofy_lms.users.models import Teacher
from lumofy_lms.users.models import User
from collections.abc import Sequence
from random import choice
from typing import Any


class UserFactory(DjangoModelFactory):
    username = factory.Faker("name")
    is_staff = factory.Faker("pybool")
    @post_generation
    def password(
        self,
        create: bool,  # noqa: FBT001
        extracted: Sequence[Any],
        **kwargs,
    ):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)  # type: ignore[attr-defined]

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """Save again the instance if creating and at least one hook ran."""
        if create and results and not cls._meta.skip_postgeneration_save:  # type: ignore[attr-defined]
            # Some post-generation hooks ran, and may have modified us.
            instance.save()

    class Meta:
        model = User
        django_get_or_create = ["username","is_staff"]


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
    specialization = factory.Faker("text", max_nb_chars=50)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)
