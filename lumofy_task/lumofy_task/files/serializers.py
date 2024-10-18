from rest_framework import serializers

from .models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ["id", "file", "file_type"]


class FileUploadDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ["id", "file", "file_type", "uploaded_at", "file_size"]
