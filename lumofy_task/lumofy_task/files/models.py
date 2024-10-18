from django.conf import settings
from django.db import models
from rest_framework.exceptions import ValidationError

# Create your models here.


def validate_file_size(file):
    max_size_mb = settings.MAX_FILE_SIZE_MB
    max_size = max_size_mb * 1024 * 1024  # Convert MB to bytes
    if file.size > max_size:
        msg = f"File size exceeds the maximum allowed size of {max_size_mb} MB."
        raise ValidationError(  # noqa: TRY003
            msg,
        )


class FileUpload(models.Model):
    file = models.FileField(upload_to="uploads/", validators=[validate_file_size])
    file_type = models.CharField(max_length=50, blank=True, null=True)  # noqa: DJ001
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.file.name}"

    def save(self, *args, **kwargs):
        self.file_size = self.file.size
        self.file_type = self.file.name.split(".")[-1].lower()
        super().save(*args, **kwargs)


