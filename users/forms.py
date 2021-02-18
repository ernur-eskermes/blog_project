from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile


class OurRegistration(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class':'class_value',
            'placeholder':"mailbox@example.com"
            })) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class':'class_value',
            'placeholder':"mailbox@example.com"
            }))        

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileAvatar(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']        
