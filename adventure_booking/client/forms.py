from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ClientDetail, ClientOffer
from froala_editor.widgets import FroalaEditor

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username',
            }),
            'email': forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'E-mail',
            }),
            'password1': forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'password',
            }),
            'password2': forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Re-type password',

            }),
            }


class ClientDetailForm(ModelForm):
    class meta:
        model = ClientDetail
        fields = "__all__"



class OfferForm(ModelForm):
     class Meta:
         model = ClientOffer
         fields = "__all__"
         widgets = {
             'trip_name': forms.TextInput(attrs={
                         'class':'form-control',
                         'placeholder':'Package Name',
             }),
             'price': forms.TextInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Price',
             }),
             'duration': forms.TextInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'duration',
             }),
             }
