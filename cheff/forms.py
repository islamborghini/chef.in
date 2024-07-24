from django import forms
from .models import Ratings

#Initializing the Rating Form (used in recipy.html template)
class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['rating']
