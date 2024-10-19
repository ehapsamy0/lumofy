from rest_framework import generics
from rest_framework import permissions
from rest_framework import response
from rest_framework import views
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .models import Enrollment
from .models import Lesson
from .serializers import CourseListSerializer
from .serializers import CourseProgressSerializer
from .serializers import CourseReadSerializer
from .serializers import CourseWriteSerializer
from .serializers import LessonReadSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonReadSerializer

class CourseListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return CourseListSerializer
        return CourseWriteSerializer

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            return Course.objects.all().select_related("teacher")
        return Course.objects.all()


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return CourseReadSerializer
        return CourseWriteSerializer

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (
                Course.objects.all()
                .select_related("teacher")
                .prefetch_related("lessons")
            )
        return Course.objects.all()


class CourseProgressView(generics.ListAPIView):
    serializer_class = CourseProgressSerializer
    permission_classes = [permissions.IsAdminUser]


    def get(self,request,pk,*args, **kwargs):
        queryset = Enrollment.objects.filter(
            course_id=self.kwargs.get("pk")
        ).select_related("student", "course")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CourseProgressSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CourseProgressSerializer(queryset, many=True)
        return response.Response(serializer.data)
