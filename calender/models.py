from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Facility


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

    category = models.CharField(choices=CG, max_length=200)
    date = models.DateField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=ST, null=True, blank=True)
    time = models.TimeField()
    duration = models.DurationField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Todo-{self.category}"