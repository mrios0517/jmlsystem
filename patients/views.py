from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect 

from .forms import PatientForm

from .models import Patient

# Create your views here.
def patient_create_view(request):
	form = PatientForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = PatientForm()
	context = {
		'form':form

	}
	return render(request, "patient_create.html", context)

