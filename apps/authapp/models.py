from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    email = models.CharField(max_length=240, blank=True, null=True, unique=True)
    balance = models.CharField(max_length=240, blank=True, null=True , default="0")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
