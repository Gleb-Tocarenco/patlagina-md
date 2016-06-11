from django.shortcuts import render,redirect
from django.http import HttpResponse
from models import Medicament
from form import MedicamentForm
# Create your views here.

def list_medicine(request):
	medicine_list=Medicament.objects.all()
	return render(request, "medicamente.html",{"medicines":medicine_list})

def get_medicament_form(request):
	m_form=MedicamentForm()
	return render(request,"medicament_form.html",{"form":m_form})

def save_medicine(request):
	if request.method == "POST":
		m_form = MedicamentForm(request.POST)
		if m_form.is_valid():
			m_form.save()
			return redirect("list_medicine")
		else:
		    return render(request,"medicament_form.html",{"form":m_form})

def home(request):
	return render(request,'home.html')

def meds(request):
	return render(request, 'meds.html')

def drugstore(request):
	return render(request, 'drugstore.html')

def signup(request):
	return render(request,'signup.html')