from django import forms
from Apis.canino.models import Perro

class PerroForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Perro

        fields = [
        'nombre',
        'sexo',
        'raza',
        'edad',
        'rescate',
        'adoptante',
        'vacuna',
        ]

        labels = {
        'nombre':'Nombre',
        'sexo':'Sexo',
        'raza':'Raza',
        'edad':'Edad',
        'rescate':'fecha de rescate o ingreso',
        'adoptante': 'Adoptante',
        'vacuna':'Vacunas',
        }

        widgets = {
        'nombre':forms.TextInput(attrs={'class':'form-control'}),
        'sexo':forms.Select(attrs={'class': 'form-control'}),
        'raza':forms.Select(attrs={'class':'form-control'}),
        'edad':forms.TextInput(attrs={'class':'form-control'}),
        'rescate':forms.TextInput(attrs={'class':'form-control'}),
        'adoptante':forms.Select(attrs={'class':'form-control'}),
        'vacuna':forms.CheckboxSelectMultiple(),
        }
