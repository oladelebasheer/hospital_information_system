from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from patients.models import Patient
from records.models import MedicalRecord
from billing.models import Bill, Payment


class Command(BaseCommand):
    help = 'Create default roles and assign permissions'

    def handle(self, *args, **kwargs):
        roles = ['Admin', 'Receptionist', 'Doctor', 'Nurse', 'Cashier', 'Management']
        groups = {}

        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            groups[role] = group

        patient_permissions = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Patient))
        record_permissions = Permission.objects.filter(content_type=ContentType.objects.get_for_model(MedicalRecord))
        bill_permissions = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Bill))
        payment_permissions = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Payment))

        groups['Receptionist'].permissions.set(patient_permissions)

        groups['Doctor'].permissions.set(record_permissions)
        groups['Nurse'].permissions.set(record_permissions.filter(codename__startswith='view'))

        groups['Cashier'].permissions.set(list(bill_permissions) + list(payment_permissions))

        groups['Management'].permissions.set([])

        self.stdout.write(self.style.SUCCESS('Roles and permissions created successfully.'))