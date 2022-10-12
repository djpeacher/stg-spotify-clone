from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-is_active"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", blank=True, null=True)
    favorite_color = models.CharField(max_length=55, blank=True, null=True)
    favorite_band = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return str(self.pk)
