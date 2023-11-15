from django.contrib import admin

from .models import Patient, Visit

class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name","dob","mobile","sex")

admin.site.register(Patient, PatientAdmin)

class VisitAdmin(admin.ModelAdmin):
    list_display = (
        "date_of_service","issue","visit_category",
    )

    fieldsets = (
        ("New Encounter",{
            "fields":("visit_category","facility","date_of_service"),
        }),
        ("Issue",{
            "fields":("issue","begin_date","end_date","diagnosis","outcome"),
            "classes":("collapse",),
        }),
    )

admin.site.register(Visit, VisitAdmin)