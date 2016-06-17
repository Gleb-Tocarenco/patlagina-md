from django.shortcuts import render, redirect

from django.http import HttpResponse

from models import Medicament, Localitate
from forms import MedicamentForm
from easy_thumbnails.files import get_thumbnailer
# Create your views here.


def list_medicine(request):
    medicine_list = Medicament.objects.all()
    return render(request, "medicamente.html", {"medicines": medicine_list})


def home(request):
    medicamente_prim = Medicament.objects.all()[:3]
    print(medicamente_prim[0].image.name)
    return render(request,
                  'home.html',
                  {'med': medicamente_prim}
                  )


def meds(request):
    medicine_list = Medicament.objects.all()
    return render(request, 'medicamente.html', {"medicines": medicine_list})


def drugstore(request):
    locations = Localitate.objects.all()
    return render(request, 'drugstore.html', {'localitati': locations})


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def diseases(request):
    return render(request, 'diseases.html')


def blog(request):
    return render(request, 'blog.html')
