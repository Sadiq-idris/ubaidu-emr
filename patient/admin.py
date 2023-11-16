from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Patient, Visit, Soap, Vitals

User = get_user_model()

class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name","dob","mobile","sex")

admin.site.register(Patient, PatientAdmin)


# soap admin
class SoapInline(admin.StackedInline):
    model = Soap
    extra = 1
    # verbose_name = "captain"

# vitals 
class VitalInline(admin.StackedInline):
    model = Vitals
    extra = 1
    verbose_name = "Vital"

class VisitAdmin(admin.ModelAdmin):
    list_display = (
        "patient","date_of_service", "provider", "issue","visit_category",
    )

    fieldsets = (
        ("New Encounter",{
            "fields":("patient","visit_category","facility", "provider", "date_of_service"),
        }),
        ("Issue",{
            "fields":("issue","begin_date","end_date","diagnosis","outcome"),
            "classes":("collapse",),
        }),
    )

    inlines = (SoapInline,VitalInline,)
       

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider":
            kwargs["queryset"] = User.objects.filter(authorized=True)
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# # custom admin page
# class VisitSite(admin.AdminSite):
#     site_header = "Appointment"

# visit_site = VisitSite(name="visitsite")


admin.site.register(Visit, VisitAdmin)


