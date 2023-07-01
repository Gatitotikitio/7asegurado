from django import forms
from .models import Contacto , item

class contactoForm(forms.ModelForm):
    
    class Meta: 
        model = Contacto
        fields= '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'

        widget = {
            "Nuevo": forms.CheckboxSelectMultiple()
        }