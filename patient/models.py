from django.db import models
from accounts.models import Facility
from django.utils import timezone


class Patient(models.Model):

    SX = (("male", "Male"), ("female", "Female"), ("other", "other"),)

    MS = (
        ("married", "Married"),
        ("single", "Single"),
        ("divorced", "Divorced"),
        ("widowed", "Widowed"),
        ("separatd", "Separeted"),
        ("domestic partner", "Domestic Partner"),
    )

    LG = (
        ("english", "English"),
        ("hausa", "Hausa"),
        ("pigin", "Pigin"),
        ("french", "French"),
    )

    RC = (
        ("black", "Black"),
        ("caucacian", "Caucacian"),
        ("asian", "Asian"),
        ("hispanic", "Hispanic"),
    )

    # who
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    sex = models.CharField(choices=SX, max_length=200)
    license_id = models.CharField(max_length=200)
    marital_status = models.CharField(choices=MS, max_length=300, help_text="optional", null=True, blank=True)

    # contact info
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.IntegerField()
    emergency_phone = models.IntegerField(help_text="phone number?")
    home_phone = models.IntegerField(help_text="phone number?", null=True, blank=True)
    mobile = models.IntegerField(help_text="patient phone number?", null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    # employer
    occupation = models.CharField(max_length=500)
    employers_numbers = models.IntegerField(null=True, blank=True)

    # status
    language = models.CharField(choices=LG, max_length=300)
    race = models.CharField( max_length=500, choices=RC)
    homeless = models.BooleanField( null=True, blank=True, help_text="optional*")


    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# visit
class Visit(models.Model):
    VC = (
        ("established patient", "Established Patient"),
        ("new patient", "New Patient"),
        ("office visit", "Office Visit"),
        ("reserved", "Reserved"),
    )

    TP = (
        ("problem", "Problem"),
        ("allergy", "Allergy"),
        ("medication", "Medication"),
        ("surgery", "Surgery"),
        ("dental", "Dental"),
    )

    OT = (
        ("unassigned", "Unassigned"),
        ("resolved", "Resolved"),
        ("improved", "Improved"),
        ("status quo", "Status quo"),
        ("worse", "Worse"),
        ("pending followup", "Pending followup"),
    )

    visit_category = models.CharField(choices=VC, max_length=300)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    date_of_service = models.DateField(default=timezone.now, null=True, blank=True)
    # add issue (optional)
    issue = models.CharField(max_length=200, choices=TP, null=True, blank=True, help_text="select one of these type title")
    begin_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True, help_text="leave blank if still active")
    diagnosis = models.TextField(null=True, blank=True)
    outcome = models.CharField(max_length=200, choices=OT, null=True, blank=True)

