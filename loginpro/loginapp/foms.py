from django import forms
from .models import registrationData
class Registrationform(forms.ModelForm):
    class Meta:
        model=registrationData
        fields='__all__'
