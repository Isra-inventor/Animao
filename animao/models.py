from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

# Course Model
class Course(models.Model):
    course_name = models.CharField(max_length=30, blank=False)
    course_description = models.TextField(blank=False)
    course_image = models.URLField(blank=False)

    course_data = models.JSONField(default=dict)