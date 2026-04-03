from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    REPORT_TYPES = (
        ('Medical', 'Medical'),
        ('Financial', 'Financial'),
        ('Administrative', 'Administrative'),
    )

    report_type = models.CharField(max_length=30, choices=REPORT_TYPES)
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_generated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} Report - {self.date_generated.date()}"