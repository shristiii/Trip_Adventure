from django import forms
from froala_editor.widgets import FroalaEditor
from django.forms import ModelForm
from .models import UserBlog

class BlogForm(ModelForm):
     class Meta:
         model = UserBlog
         fields = ['title','content','image',]
         # fields = "__all__"
         # widgets = {
         #     'user': forms.TextInput(attrs={
         #                 'class':'form-control',
         #                 'placeholder':'Username',
         #                'disabled',
         #     }),
         #     }
