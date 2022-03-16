from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Profile
from django.forms.models import ModelForm
from .models import Book 
from django.forms.widgets import FileInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ('title','author','pdf')




