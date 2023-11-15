from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe



class CustomUser(AbstractUser):

    CH = (
        ("accounting", "Accounting"),
        ("administrators" ,"Administrators"),
        ("clinicians", "Clinicians"),
        ("front office", "Front Office"),
        ("physicians", "Physicians"),
    )


    federal_tax_id = models.CharField(max_length=200, null=True, blank=True)
    authorized = models.BooleanField(null=True, blank=True)
    job_description = models.CharField(max_length=3000, null=True, blank=True)
    access_control = models.CharField(choices=CH, max_length=200, null=True, blank=True)
    additional_info = models.TextField(max_length=5000, null=True, blank=True)
    user_pic = models.ImageField(upload_to="images/", null=True, blank=True)

    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='50' height='50' />" % (self.user_pic))
    
    image_tag.allow_tags = True


# facilities
class Facility(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    federal_EIN = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Facilities"

    def __str__(self):
        return self.name
