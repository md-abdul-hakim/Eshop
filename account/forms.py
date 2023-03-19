from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude = ('user', )

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password')