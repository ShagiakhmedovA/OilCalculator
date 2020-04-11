from django import forms
from .models import Post, Calculation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'title', 'text', 'picture'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email'


class CalculationForm(forms.ModelForm):

    class Meta:
        model = Calculation
        fields = 'V1', 'V2', 'RZAB1', 'RZAB2', 'RPL'
