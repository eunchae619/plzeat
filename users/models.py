import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

# Create your models here.


class User(AbstractUser):
    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
    )

    email_verified = models.BooleanField(default=True)
    email_secret = models.CharField(max_length=120, default="", blank=True)
    nickname = models.CharField(max_length=100, null=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    email_verified = models.BooleanField(default=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify PLZEAT Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        splited = self.email.split("@")
        splited = splited[0]
        self.nickname = splited
        super().save(*args, **kwargs)
