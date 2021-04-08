from django import forms
from .models import *

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        exclude = ['timestamp_out','comment']

class SalidaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        exclude = ['timestamp_out']