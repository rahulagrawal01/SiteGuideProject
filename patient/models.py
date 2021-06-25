from django.db import models
from django.urls import reverse
# Create your models here.
class Patient(models.Model):
    First_Name=models.CharField(max_length=40)
    Last_Name=models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Disease=models.CharField(max_length=50)
    Doctor_Name=models.CharField(max_length=50)
    Doctor_Fees=models.IntegerField(default=500)
    Start_dat=models.DateField(auto_now=True)
    Age=models.IntegerField(default=1)

    def __str__(self):
        return self.First_Name


    def get_absolute_url(self):
        return reverse("showpatient1")
    

        