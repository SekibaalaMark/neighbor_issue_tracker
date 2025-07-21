# serializers.py
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            password=validated_data['password'],
        )

        # Send verification email
        verification_link = f"http://localhost:8000/api/verify-email/{user.verification_code}/"

        send_mail(
            subject='Verify your email',
            message=f'Hi {user.username},\n\nClick the link to verify your email: {verification_link}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return user
