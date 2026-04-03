from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

class Doctor(models.Model):
    full_name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='records')
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescription = models.TextField(blank=True, null=True)
    visit_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.visit_date}"