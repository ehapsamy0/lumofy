from django.contrib import admin

# Register your models here.
from .models import Lesson,Course,Enrollment,LessonCompletion

admin.site.register(Course)
admin.site.register(Lesson)


admin.site.register(Enrollment)
admin.site.register(LessonCompletion)
