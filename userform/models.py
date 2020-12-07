from django.db import models
from phone_field import PhoneField

from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class ForLogin(models.Model):

    name = models.CharField(blank=False, max_length=50)
    dob = models.DateField(blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    


    def __str__(self):
        return self.name


    