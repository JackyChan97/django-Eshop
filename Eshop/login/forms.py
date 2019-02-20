
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
