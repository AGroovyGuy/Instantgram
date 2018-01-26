from django.forms import forms
from django import forms


class PhotoUploadForm(forms.Form):
    photo = forms.ImageField()
    description = forms.CharField()



class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=150,  label="nickname")
    password = forms.CharField(max_length=150,  label="Hasło", widget=forms.PasswordInput)


class CreateAccountForm(forms.Form):
    nickname = forms.CharField(max_length=100, label="Nickname")
    password = forms.CharField(max_length=150, label="Hasło", widget=forms.PasswordInput)
    mail = forms.CharField(max_length=150, label="E-mail")