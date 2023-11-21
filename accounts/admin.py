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
        "username",
        "image_tag",
        "email",
        "is_staff",
        "access_control",
    ]

    fieldsets = UserAdmin.fieldsets + (("info",{
        "fields":(
            "user_pic",
            "federal_tax_id",
            "job_description","access_control",
            "additional_info",
        ),
    }),)

    add_fieldsets = UserAdmin.add_fieldsets + (("info",{
        "fields":(
            "user_pic",
            "first_name","last_name","email",
            "federal_tax_id",
            "job_description","access_control",
            "additional_info",
        ),
    }),)

admin.site.register(CustomUser, CustomUserAdmin)


User = get_user_model()
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_superuser=True)
    
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Facility, FacilityAdmin)