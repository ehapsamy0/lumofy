from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import FileUploadFilter
from .models import FileUpload
from .serializers import FileUploadDetailsSerializer
from .serializers import FileUploadSerializer

# Create your views here.


class FileUploadView(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


class FileListView(generics.ListAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FileUploadFilter

    def get_queryset(self):
        file_type = self.request.query_params.get("file_type", None)
        if file_type:
            return self.queryset.filter(file_type=file_type.lower())
        return self.queryset


class FileDetailView(generics.RetrieveAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadDetailsSerializer
