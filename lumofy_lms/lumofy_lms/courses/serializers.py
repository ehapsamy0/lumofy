from rest_framework import serializers

from .services import create_course, update_course
from lumofy_lms.users.serializers import TeacherSerializer,StudentSerializer

from .models import Course
from .models import Enrollment
from .models import Lesson
from .models import LessonCompletion


class LessonWriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Lesson
        fields = "__all__"
        extra_kwargs = {
            "course": {"required": False},
        }


class LessonReadSerializer(LessonWriteSerializer):
    class Meta(LessonWriteSerializer.Meta):
        pass


class CourseWriteSerializer(serializers.ModelSerializer):
    lessons = LessonWriteSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        return create_course(validated_data)

    def update(self, instance, validated_data):
        update_course(instance, validated_data)
        return super().update(instance, validated_data)


class CourseListSerializer(CourseWriteSerializer):
    teacher = TeacherSerializer()

    class Meta(CourseWriteSerializer.Meta):
        pass


class CourseReadSerializer(CourseWriteSerializer):
    lessons = LessonWriteSerializer(many=True, read_only=True)
    teacher = TeacherSerializer()

    class Meta(CourseWriteSerializer.Meta):
        pass


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"


class LessonCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonCompletion
        fields = "__all__"




class CourseProgressSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source="course.name")
    student = serializers.CharField(source="student.user")
    status = serializers.CharField(source = "get_status_display")
    class Meta:
        model = Enrollment
        fields = "__all__"
