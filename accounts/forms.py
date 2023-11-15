from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        models = CustomUser
        fields = (
            "username","first_name",
            "last_name","email",
            "federal_tax_id","authorized",
            "job_description","access_control",
            "additional_info",
            )

        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        models = CustomUser
        fields = (
            "username","first_name",
            "last_name","email",
            "federal_tax_id","authorized",
            "job_description","access_control",
            "additional_info",
        )