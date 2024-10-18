from django.urls import path

from .views import FileDetailView
from .views import FileListView
from .views import FileUploadView

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file-upload"),
    path("", FileListView.as_view(), name="file-list"),
    path("<int:pk>/", FileDetailView.as_view(), name="file-detail"),
]
