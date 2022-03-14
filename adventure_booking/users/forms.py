from django import forms
from froala_editor.widgets import FroalaEditor
from django.forms import ModelForm
from .models import UserBlog

class BlogForm(ModelForm):
     class Meta:
         model = UserBlog
         fields = "__all__"
