import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from lumofy_lms.courses.models import Course
from lumofy_lms.courses.models import Enrollment
from lumofy_lms.courses.models import Lesson
from lumofy_lms.courses.models import LessonCompletion
from lumofy_lms.users.models import Student
from lumofy_lms.users.models import Teacher
from lumofy_lms.users.models import User
from lumofy_lms.users.tests.factories import StudentFactory
from lumofy_lms.users.tests.factories import TeacherFactory


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    teacher = factory.SubFactory(TeacherFactory)
    attendance_count = factory.Faker("random_number", digits=2)
    completion_count = factory.Faker("random_number", digits=2)
    created_at = factory.LazyFunction(timezone.now)


class LessonFactory(DjangoModelFactory):
    class Meta:
        model = Lesson

    title = factory.Faker("word")
    content = factory.Faker("text")
    course = factory.SubFactory(CourseFactory)
    attendance_count = factory.Faker("random_number", digits=1)


class EnrollmentFactory(DjangoModelFactory):
    class Meta:
        model = Enrollment

    student = factory.SubFactory(StudentFactory)
    course = factory.SubFactory(CourseFactory)
    status = factory.Iterator(
        [
            Enrollment.STATUS.ACTIVE,
            Enrollment.STATUS.COMPLETED,
            Enrollment.STATUS.FAILED,
        ]
    )


class LessonCompletionFactory(DjangoModelFactory):
    class Meta:
        model = LessonCompletion

    student = factory.SubFactory(StudentFactory)
    lesson = factory.SubFactory(LessonFactory)
    completion_date = factory.LazyFunction(timezone.now)
