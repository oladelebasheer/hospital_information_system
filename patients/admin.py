from django.contrib import admin
from .models import Patient
from django.contrib.auth.models import Group, Permission

admin.site.register(Patient)

def assign_permissions():
    receptionist = Group.objects.get(name='Receptionist')
    doctor = Group.objects.get(name='Doctor')
    cashier = Group.objects.get(name='Cashier')

    receptionist.permissions.add(
        Permission.objects.get(codename='can_register_patient'),
    )

    doctor.permissions.add(
        Permission.objects.get(codename='can_view_patient'),
    )
    