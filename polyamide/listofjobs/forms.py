from pagedown.widgets import PagedownWidget 
from django import forms
from models import joblisting

class JobDescriptionForm(forms.ModelForm):
    description_md= forms.CharField(widget=PagedownWidget())

    class Meta:
        model=joblisting

