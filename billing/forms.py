from django import forms
from .models import Bill, Payment

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient', 'amount', 'status']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter bill amount'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bill', 'amount_paid', 'payment_method']
        widgets = {
            'bill': forms.Select(attrs={
                'class': 'form-select'
            }),
            'amount_paid': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount paid'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-select'
            }),
        }