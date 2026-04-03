from django.db.models import Q
from .models import MedicalRecord
from .forms import MedicalRecordForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalRecord
from .forms import MedicalRecordForm


def record_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'records/record_list.html', {'records': records})


def record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'records/record_detail.html', {'record': record})


def add_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'records/add_record.html', {'form': form})


def edit_record(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, 'records/edit_record.html', {'form': form, 'record': record})


def delete_record(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'records/delete_record.html', {'record': record})


def record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'records/record_detail.html', {'record': record})

def record_list(request):
    query = request.GET.get('q')
    records = MedicalRecord.objects.select_related('patient', 'doctor').all()

    if query:
        records = records.filter(
            Q(patient__full_name__icontains=query) |
            Q(doctor__full_name__icontains=query) |
            Q(diagnosis__icontains=query) |
            Q(treatment__icontains=query) |
            Q(prescription__icontains=query)
        )

    return render(request, 'records/record_list.html', {'records': records})


def add_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = MedicalRecordForm()

    return render(request, 'records/add_record.html', {'form': form})