from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.decorators import role_required
from .models import Patient
from .forms import PatientForm


@login_required
@role_required(['Admin', 'Receptionist', 'Doctor', 'Nurse'])
def patient_list(request):
    query = request.GET.get('q')

    if query:
        patients = Patient.objects.filter(
            Q(full_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        patients = Patient.objects.all()

    context = {
        'patients': patients,
        'query': query,
    }
    return render(request, 'patients/patient_list.html', context)


@login_required
@role_required(['Admin', 'Receptionist'])
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'patients/add_patient.html', {'form': form})


@login_required
@role_required(['Admin', 'Receptionist', 'Doctor', 'Nurse'])
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})