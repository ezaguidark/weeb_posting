from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser # el modelo que creamos con los datos que queremos
        fields = ('username','email' ,'age', 'profile_image', 'description')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','email' ,'age', 'profile_image', 'description')