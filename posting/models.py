from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    programme = models.CharField(max_length=50)  # , choices=PROGRAMME_CHOICES)
    # , choices=DEPARTMENT_CHOICES)
    discipline = models.CharField(max_length=50)
