from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
def Home(request):
    return render(request,'patient/Home.html')

class PatientList(ListView):
    model=Patient


class AddPatient(CreateView):
    model = Patient
    fields='__all__'
    template_name = "patient/AddPatient.html"

class UpdatePatient(ListView):
    template_name = "patient/updatepatient.html"
    model = Patient

class UpdatePatientpk(UpdateView):
    model = Patient
    fields='__all__'
    
class DeletePatient(ListView):
    template_name = "patient/deletepatient.html"
    model = Patient

class DeletePatientpk(DeleteView):
    model = Patient
    success_url=reverse_lazy('showpatient1')
