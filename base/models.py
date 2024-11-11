from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use hashed storage
    country = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    projects = models.TextField(blank=True)
    skills = models.TextField(blank=True)  # Store skills as a comma-separated string or JSON
    experience = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.email


class StartupProfile(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    website_url = models.URLField(blank=True)
    skills_required = models.TextField(blank=True)  # Store as comma-separated or JSON
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)

    def __str__(self):
        return self.company_name


