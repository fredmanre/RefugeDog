from django import forms
from Apis.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Persona

        fields = [
        'nombre',
        'apellidos',
        'edad',
        'telefono',
        'email',
        'domicilio',
        ]

        labels = {
        'nombre':'Nombre',
        'apellidos':'Apellidos',
        'edad':'Edad',
        'telefono':'Telefono',
        'email':'Correo electronico',
        'domicilio':'Direccion habitacion',
        }

        widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca un nombre'}),
        'apellidos': forms.TextInput(attrs={'class':'form-control'}),
        'edad': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'min':'18', 'max':'75'}),
        'telefono': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
        'email': forms.TextInput(attrs={'class':'form-control', 'type':'email'}),
        'domicilio': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PersonaForm, self).clean()
        return cleaned_data


class SolicitudForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Solicitud

        fields = [
        'numero_caninos',
        'razon',
        ]

        labels = {
        'numero_caninos':'Numero de mascotas a adoptar',
        'razon':'Justificacion',
        }

        widgets = {
        'numero_caninos': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'min':'0', 'max':'5'}),
        'razon': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
        }

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(SolicitudForm, self).clean()
        return cleaned_data
