from django.shortcuts import render, redirect
from .models import Bill, Payment
from .forms import BillForm, PaymentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required

def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()

    return render(request, 'billing/add_bill.html', {'form': form})
@login_required
@role_required(['Admin', 'Cashier'])
def bill_list(request):
    bills = Bill.objects.select_related('patient').all()
    return render(request, 'billing/bill_list.html', {'bills': bills})


@login_required
@role_required(['Admin', 'Cashier'])
def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/add_bill.html', {'form': form})


@login_required
@role_required(['Admin', 'Cashier'])
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            bill = payment.bill

            total_paid = sum(p.amount_paid for p in bill.payments.all())
            if total_paid >= bill.amount:
                bill.status = 'Paid'
            else:
                bill.status = 'Pending'
            bill.save()

            return redirect('bill_list')
    else:
        form = PaymentForm()
    return render(request, 'billing/add_payment.html', {'form': form})

def bill_list(request):
    bills = Bill.objects.select_related('patient').all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/add_bill.html', {'form': form})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            bill = payment.bill

            total_paid = sum(p.amount_paid for p in bill.payments.all())
            if total_paid >= bill.amount:
                bill.status = 'Paid'
            else:
                bill.status = 'Pending'
            bill.save()

            return redirect('bill_list')
    else:
        form = PaymentForm()
    return render(request, 'billing/add_payment.html', {'form': form})