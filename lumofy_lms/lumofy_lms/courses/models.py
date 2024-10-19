from django.db import models
from django.utils.translation import gettext_lazy as _

from lumofy_lms.users.models import Student
from lumofy_lms.users.models import Teacher

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    attendance_count = models.BigIntegerField(default=0)
    completion_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    attendance_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    class STATUS(models.IntegerChoices):
        ACTIVE = 1, _("Active")
        COMPLETED = 2, _("Completed")
        FAILED = 3, _("Failed")

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
        choices=STATUS.choices, default=STATUS.ACTIVE
    )

    def __str__(self):
        return f"{self.student.user} - {self.course.name}"


class LessonCompletion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completion_date = models.DateTimeField()

    def __str__(self):
        return f"{self.student.user.first_name} - {self.lesson.title}"
