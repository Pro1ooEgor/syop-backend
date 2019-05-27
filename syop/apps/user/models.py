from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    token = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = [['email']]

