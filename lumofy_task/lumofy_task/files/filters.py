import django_filters

from .models import FileUpload


class FileUploadFilter(django_filters.FilterSet):
    file_type = django_filters.CharFilter(field_name="file_type", lookup_expr="iexact")

    class Meta:
        model = FileUpload
        fields = ["file_type"]
