from django import forms
from .models import Photo



class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["photo", "description"]


class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=150,  label="nickname")
    password = forms.CharField(max_length=150,  label="Hasło", widget=forms.PasswordInput)
