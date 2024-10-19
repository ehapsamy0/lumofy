from django.urls import path

from .views import CourseListCreateAPIView
from .views import CourseProgressView
from .views import CourseRetrieveUpdateDestroyAPIView
from .views import LessonListAPIView

app_name = "course"
urlpatterns = [
    path("", CourseListCreateAPIView.as_view(), name="courses-list-create"),
    path(
        "<int:pk>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
        name="update-delete-course",
    ),
    path("<int:pk>/progress/", CourseProgressView.as_view(), name="course-progress"),
    path("lessons/", LessonListAPIView.as_view(), name="list-lessons"),
]
