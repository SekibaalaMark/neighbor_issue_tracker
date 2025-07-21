# models.py
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('UECDL', 'UECDL'),
        ('NWSC', 'NWSC'),
        ('UNRA', 'UNRA'),
        ('NEMA', 'NEMA'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='resident')
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True)
    
    is_verified = models.BooleanField(default=False)  # 👈 Add this
    verification_code = models.UUIDField(default=uuid.uuid4)  # 👈 Add this

    def __str__(self):
        return self.username
