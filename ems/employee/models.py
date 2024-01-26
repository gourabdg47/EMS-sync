from django.db import models

class Employee(models.Model):
    
    # Personal Information
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # Contact Information
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    zip_postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    # Employment Details
    employee_id = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    manager_supervisor_name = models.CharField(max_length=100)
    start_date = models.DateField()

    # Account Information
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    # Identification Information
    ssn_or_national_id = models.CharField(max_length=50, blank=True)

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100)
    relationship_to_employee = models.CharField(max_length=50)
    emergency_contact_phone_number = models.CharField(max_length=15)

    # Tax Information
    TAX_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married')
    ]
    tax_filing_status = models.CharField(max_length=10, choices=TAX_STATUS_CHOICES)
    withholding_allowances = models.IntegerField()

    # Banking Information
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    routing_number = models.CharField(max_length=50)

    # Benefits Enrollment
    health_insurance_enrollment = models.BooleanField(default=False)
    retirement_plan_enrollment = models.BooleanField(default=False)

    # Skills and Qualifications
    education_level = models.CharField(max_length=100)
    degrees_certifications = models.CharField(max_length=200)
    skills_expertise = models.TextField()

    # Preferences
    preferred_language = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)

    # Terms and Conditions
    terms_conditions_accepted = models.BooleanField()

    # Verification
    captcha_verified = models.BooleanField()

    # Optional
    ETHNICITY_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
        ('asian', 'Asian'),
        ('hispanic', 'Hispanic'),
        ('other', 'Other')
    ]
    ethnicity = models.CharField(max_length=20, choices=ETHNICITY_CHOICES, blank=True)
    disability_status = models.BooleanField(default=False)
    veteran_status = models.BooleanField(default=False)

    # Confirmation
    receive_notifications = models.BooleanField(default=False)

    # Agreement
    agreement_accepted = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name