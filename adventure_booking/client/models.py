from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.

class ClientDetail(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.company_name


class ClientOffer(models.Model):
    user = models.CharField(max_length=200,null=True)
    trip_name = models.CharField(max_length=200,null=True)
    trip_desc = FroalaField()
    image = models.ImageField(upload_to="offer/", null = True)
    price = models.CharField(max_length=200,null=True)
    duration = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.trip_name


class ClientBooking(models.Model):
    user = models.CharField(max_length=200,null=True)
    full_name = models.CharField(max_length=200,null=True)
    package_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    no_of_person = models.CharField(max_length=200,null=True)
    arraival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)
    condition= [
    ('confirmed', 'confirmed'),
    ('cancled', 'cancled'),
    ('null', 'null'),
    ]
    confirmance=models.CharField(max_length=12,choices=condition,default='null')
    def __str__(self):
        return self.full_name
