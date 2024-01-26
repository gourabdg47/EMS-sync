from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Company(models.Model):
    # Company Information
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    # Contact Information
    contact_person_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_address = models.CharField(max_length=200)

    # Account Information
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    # Company Profile
    industry_type = models.CharField(max_length=50)
    company_size = models.IntegerField()
    company_description = models.TextField()
    website_url = models.URLField(blank=True)

    # Additional Information
    tax_id = models.CharField(max_length=50, blank=True)
    industry_certification = models.CharField(max_length=100, blank=True)

    # Preferences
    preferred_language = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)

    # Terms and Conditions
    terms_conditions_accepted = models.BooleanField()

    # Verification
    captcha_verified = models.BooleanField()

    # Optional
    social_media_links = models.CharField(max_length=200, blank=True)
    additional_contact_info = models.CharField(max_length=200, blank=True)

    # Confirmation
    receive_notifications = models.BooleanField(default=False)

    # Agreement
    agreement_accepted = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
