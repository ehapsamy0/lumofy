from django.db import transaction

from .models import Course
from .models import Lesson
from rest_framework.exceptions import NotFound

@transaction.atomic
def create_course(validated_data):
    lessons = validated_data.pop("lessons", [])

    course = Course.objects.create(**validated_data)
    course_lessons = []
    for lesson in lessons:
        course_lessons.append(  # noqa: PERF401
            Lesson(
                title=lesson.get("title"),
                content=lesson.get("content"),
                course=course,
                attendance_count=lesson.get("attendance_count"),
            )
        )
    Lesson.objects.bulk_create(course_lessons)

    return course


@transaction.atomic
def update_course(instance, validated_data):
    lessons = validated_data.pop("lessons", [])
    if lessons:
        existing_lessons = instance.lessons.all()
        incoming_lesson_ids = set()
        new_course_lessons = []
        for lesson_data in lessons:
            lesson_id = lesson_data.get("id", None)
            if lesson_id:
                try:
                    lesson_instance = Lesson.objects.get(id=lesson_id, course=instance)
                except:  # noqa: E722
                    raise NotFound()  # noqa: B904
                for attr, value in lesson_data.items():
                    setattr(lesson_instance, attr, value)
                lesson_instance.save()
                incoming_lesson_ids.add(lesson_id)


            else:
                new_course_lessons.append(
                    Lesson(
                        title=lesson_data.get("title"),
                        content=lesson_data.get("content"),
                        course=instance,
                        attendance_count=lesson_data.get("attendance_count", 0),
                    )
                )
        lessons_to_delete = existing_lessons.exclude(id__in=incoming_lesson_ids)
        lessons_to_delete.delete()
        Lesson.objects.bulk_create(new_course_lessons)
    return instance
