from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        DEVELOPER = "developer", "Developer"
        CLIENT = "client", "Client"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.DEVELOPER,
    )

   
    class Membership(models.TextChoices):
        FREE = "free", "Free"
        PLUS = "plus", "Plus"
        PRO = "pro", "Pro"


    membership_plan = models.CharField(
        max_length=10, choices=Membership.choices, default=Membership.FREE
    )



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    headline = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    skills = models.TextField(
        help_text="Comma-separated skills",
        blank=True
    )

    goals = models.TextField(blank=True)

    experience = models.TextField(
        help_text="User work experience",
        blank=True
    )

    location = models.CharField(max_length=100, blank=True)

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def skills_list(self):
        return [skill.strip() for skill in self.skills.split(",") if skill]

    def __str__(self):
        return f"{self.user.username}'s Profile"