from django import forms
from .models import Voter


class VoterForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Voter
        fields = ['name', 'image']