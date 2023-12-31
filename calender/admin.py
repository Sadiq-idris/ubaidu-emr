from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Calender

User = get_user_model()

class CalenderAdmin(admin.ModelAdmin):
    list_display = ("category","provider","status", "room_number", "date", "time", )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider":
            kwargs["queryset"] = User.objects.filter(access_control="physicians")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        elif request.user.access_control == "front office" or  request.user.access_control == "clinicians" :
            return qs

        return qs.filter(provider=request.user)

admin.site.register(Calender, CalenderAdmin)

# ADMIN PANEL COSTUMIZATION 

# admin.site.unregister(Group)

admin.site.site_header = "Ubaidu-emr"

admin.site.site_title = "Ubaidu-emr"

