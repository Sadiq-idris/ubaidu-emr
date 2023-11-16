from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Facility
from patient.models import Patient


class Calender(models.Model):

    CG = (
        ("established patient", "Established Patient"),
        ("in office", "In Office"),
        ("lunch", "Lunch"),
        ("new patient", "New Patient"),
        ("office visit", "Office Visit"),
        ("put of office", "Out Of Office"),
    )

    ST = (
        (" ", " "),
        ("reminder done", "* Reminder Done"),
        ("chart pulled", "+ Chart Pulled"),
        ("cancelled", "x Cancelled"),
        ("arrived", "@ Arrived"),
    )

    RM = (
        ("room 1", "Room 1"),
        ("room 2", "Room 2"),
        ("room 3", "Room 3"),
    )

    category = models.CharField(choices=CG, max_length=200)
    date = models.DateField(null=True, blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=200, choices=ST, null=True, blank=True)
    room_number = models.CharField(max_length=200, choices=RM, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    comments = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        verbose_name = "Appointment"
        

    def __str__(self):
        return f"Todo-{self.category}"