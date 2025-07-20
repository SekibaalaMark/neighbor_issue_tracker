from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('UECDL', 'UECDL'),
        ('NWSC', 'NWSC'),
        ('UNRA', 'UNRA'),
        ('NEMA', 'NEMA'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='resident')

    def __str__(self):
        return self.role
