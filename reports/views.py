from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from records.models import MedicalRecord
from billing.models import Bill, Payment
from accounts.decorators import role_required

from django.shortcuts import render

def dashboard(request):
    return render(request, 'reports/dashboard.html')

def reports_page(request):
    return render(request, 'reports/reports_page.html')

@login_required
def reports_page(request):
    total_patients = Patient.objects.count()
    total_records = MedicalRecord.objects.count()
    total_bills = Bill.objects.count()
    total_payments = Payment.objects.count()

    recent_patients = Patient.objects.order_by('-id')[:5]
    recent_bills = Bill.objects.select_related('patient').order_by('-id')[:5]
    recent_payments = Payment.objects.select_related('bill', 'bill__patient').order_by('-id')[:5]

    context = {
        'total_patients': total_patients,
        'total_records': total_records,
        'total_bills': total_bills,
        'total_payments': total_payments,
        'recent_patients': recent_patients,
        'recent_bills': recent_bills,
        'recent_payments': recent_payments,
    }
    return render(request, 'reports/reports_page.html', context)