from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Facility

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = CustomUser
    list_display = [
        "image_tag",
        "username",
        "email",
        "is_staff",   
    ]

    fieldsets = UserAdmin.fieldsets + (("info",{
        "fields":(
            "user_pic",
            "federal_tax_id","authorized",
            "job_description","access_control",
            "additional_info",
        ),
    }),)

    add_fieldsets = UserAdmin.add_fieldsets + (("info",{
        "fields":(
            "user_pic",
            "first_name","last_name","email",
            "federal_tax_id","authorized",
            "job_description","access_control",
            "additional_info",
        ),
    }),)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Facility)