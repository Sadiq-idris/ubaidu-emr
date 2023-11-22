from django.shortcuts import render, get_object_or_404, redirect
from patient.models import InsuranceCompany
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, "index/index.html")


@login_required
def insurance(request):
    # insurances = get_object_or_404(InsuranceCompany)
    insurances = InsuranceCompany.objects.all()

    if request.user.is_superuser:

        return render(request, "index/insurance.html",{
            "insurances": insurances,
        })

    else:

        return redirect("home")