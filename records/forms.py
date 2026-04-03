from django import forms
from .models import MedicalRecord


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'treatment', 'prescription']

        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select'
            }),

            'doctor': forms.Select(attrs={
                'class': 'form-select'
            }),

            'diagnosis': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter diagnosis'
            }),

            'treatment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter treatment'
            }),

            'prescription': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter prescription (optional)'
            }),
        }