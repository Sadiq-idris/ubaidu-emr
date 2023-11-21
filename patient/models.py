from django.db import models
from accounts.models import Facility
from django.utils import timezone
from django.contrib.auth import get_user_model


# patient model
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

# prescription model   
class Prescription(models.Model):

    MU = (
        ("mg","mg"),
        ("mg/1cc","mg/1cc"),
        ("mg/2cc","mg/2cc"),
        ("mg/3cc","mg/3cc"),
        ("mg/4cc","mg/4cc"),
        ("mg/5cc","mg/5cc"),
        ("mcg","mcg"),
        ("gram","gram"),
    )

    IN = (
        ("suspension","suspension"),
        ("tablet","tablet"),
        ("capsule","capsule"),
        ("solution","solution"),
        ("tsp","tsp"),
        ("ml","ml"),
    )

    RF = (
        ("01","01"),("02","02"),("03","03"),("04","04"),
        ("05","05"),("06","06"),("07","07"),("08","08"),
        ("09","09"),("10","10"),("11","11"),("12","12"),
        ("13","13"),("14","14"),("15","15"),("16","16"),
        ("17","17"),("18","18"),("19","19"),("20","20"),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    currently_active = models.BooleanField()
    starting_date = models.DateField(default=timezone.now)
    provider = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    drug = models.CharField(max_length=200)
    quantity = models.IntegerField()
    medicine_units = models.CharField(max_length=200, choices=MU)
    take = models.IntegerField()
    _in = models.CharField(max_length=200, choices=IN)
    refills = models.CharField(max_length=200, choices=RF)
    notes = models.TextField(null=True, blank=True)
    add_to_medication_list = models.BooleanField()




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

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_category = models.CharField(choices=VC, max_length=300)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    provider = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_of_service = models.DateField(default=timezone.now, null=True, blank=True)
    # add issue (optional)
    issue = models.CharField(max_length=200, choices=TP, null=True, blank=True, help_text="select one of these type title")
    begin_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True, help_text="leave blank if still active")
    diagnosis = models.TextField(null=True, blank=True)
    outcome = models.CharField(max_length=200, choices=OT, null=True, blank=True)

# CATEGORY OF ENCOUNTER

# soap
class Soap(models.Model):
    encounter = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name="soap")
    subjective = models.TextField(null=True, blank=True)
    objective = models.TextField(null=True, blank=True)
    assessment = models.TextField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)

# vitals
class Vitals(models.Model):
    TL = (
        ("",""),
        ("oral","Oral"),
        ("tympanic membrane", "Tympanic Membrane"),
        ("rectal","Rectal"),
        ("auxillary","Auxillary"),
        ("temporal artery", "Temporal Artery"),
    )

    encounter = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name="vital")
    weight_in_lbs = models.FloatField(null=True, blank=True)
    weight_in_kg = models.FloatField(null=True, blank=True)
    height_in_cm = models.FloatField(null=True, blank=True)
    BP_systolic_mmkg = models.FloatField(null=True, blank=True)
    BP_diastolic_mmkg = models.FloatField(null=True, blank=True)
    pulse_per_min = models.FloatField(null=True, blank=True)
    respiration_per_min = models.FloatField(null=True, blank=True)
    temperature_f = models.FloatField(null=True, blank=True)
    temperature_c = models.FloatField(null=True, blank=True)
    temp_location = models.CharField(choices=TL, max_length=200, null=True, blank=True)
    oxygen_saturation_percentage = models.FloatField(null=True, blank=True)
    head_circumference_cm = models.FloatField(null=True, blank=True)
    waist_circumference_cm = models.FloatField(null=True, blank=True)
    BMI_kg_per_m2 = models.FloatField(null=True, blank=True)
    BMI_status_type = models.CharField(max_length=200, null=True, blank=True)
    other_notes = models.CharField(max_length=200, null=True, blank=True)
