from django import forms
from apps.rescatado.models import Rescatado

class RescatadoForm(forms.ModelForm):
    
    class Meta:
        model = Rescatado

        #lista que contiene los campos del modelo que queremo
    #    utilizar en el formulario
        fields = [
            'nombre',
            'descripcion',
            'fotografia',
            'raza',
            'estado',
        ]
        #etiquetas que van a tener para pintar el formulario
        #utilizando un diccionario
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'fotografia': 'Fotografía',
            'raza': 'Raza Predominante',
            'estado': 'Estado',
        }
        #la forma en que se pintan las etiquetas html
        # #
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'input-field'}),
            'descripcion': forms.TextInput(attrs={'class':'input-field'}),
            'fotografia': forms.TextInput(attrs={'class':'input-field'}),
            'raza': forms.Select(attrs={'class':'select'}),
            'estado': forms.Select(attrs={'class':'select'}),
        }