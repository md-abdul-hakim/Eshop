from django import forms
from other.models import UserContact


class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = '__all__'