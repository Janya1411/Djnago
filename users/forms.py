# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ChoiceField
from .models import CustomUser, Profile
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    Profession = (
        ('', 'Choose...'),
        ('NA', 'NGO-Activist'),
        ('US', 'User'),
        ('HP', 'Help-group')
    )
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    prof: ChoiceField = forms.ChoiceField(choices=Profession)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'prof']

    def clean_password2(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match")
        return password

    def clean_email(self):

        cleaned_data = super(UserCreationForm, self).clean()
        email = self.cleaned_data.get('email')
        email_error = "Email Already exists"
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(email_error)
        return email

    def clean_username(self):

        cleaned_data = super(UserCreationForm, self).clean()
        username = self.cleaned_data.get('username')
        email_error = "Username Already exists"
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(email_error)
        return username


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'prof')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['prof', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
