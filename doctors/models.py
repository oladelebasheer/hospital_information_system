from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name