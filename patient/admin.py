from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import (Patient, Visit, Soap, Vitals,
 Prescription, InsuranceCompany, CheckOut)

User = get_user_model()

# prescription stackedline to be display in patient detail page
class PrescriptionInline(admin.StackedInline):
    model = Prescription
    extra = 0

# ------------------------------------------- patient  -------------------------------
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name","dob","mobile","sex")
    fieldsets = (
        ("Who",{
            "fields":("first_name","last_name","dob","sex","license_id","marital_status")
        }),
        ("Contact",{
            "fields":("address","city","state","country","postal_code",
            "emergency_phone","home_phone","mobile","contact_email",),
        }),
        ("Employer",{
            "fields":("occupation","employers_numbers"),
        }),
        ("Status",{
            "fields":("language","race","homeless"),
        }),
        ("Insurance Company",{
            "fields":("insurance_company",),
        }),
    )
    search_fields = ["first_name"]
    ordering = ["id"]
    list_filter = ["sex"]

    inlines = (PrescriptionInline,)

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

# checkout 
class CheckOutInline(admin.StackedInline):
    model = CheckOut
    extra = 0

#  ---------------------------------------- visit admin -----------------------------------
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        "patient","date_of_service", "provider", "issue","visit_category",
    )

    fieldsets = (
        ("Encounter",{
            "fields":("patient","visit_category","facility", "provider", "date_of_service"),
        }),
        ("Issue",{
            "fields":("issue","begin_date","end_date","diagnosis","outcome"),
            "classes":("collapse",),
        }),
    )

    inlines = (SoapInline,VitalInline,CheckOutInline)
       

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider":
            kwargs["queryset"] = User.objects.filter(access_control="physicians")
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# ----------------------- prescription admin -------------------------------
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("drug", "quantity", "medicine_units","take", "_in", "provider","patient",)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider":
            kwargs["queryset"] = User.objects.filter(access_control="physicians")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Prescription, PrescriptionAdmin)


admin.site.register(Visit, VisitAdmin)


# insurance company



admin.site.register(InsuranceCompany)
