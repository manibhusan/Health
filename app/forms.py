from django import forms

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True)
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password1 = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
