from django import forms
from django.contrib.auth.models import User
from .models import NewUser

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = '__all__'
