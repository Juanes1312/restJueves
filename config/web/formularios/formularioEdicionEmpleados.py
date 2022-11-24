from django import forms

class FormularioEdicionEmpleados(forms.Form):

    contacto = forms.CharField(
        widget = forms.TextInput(attrs = {'class':'form-control mb-3'}),
        required = True,
        max_length = 20
    )
    
    salario = forms.CharField(
        widget = forms.NumberInput(attrs = {'class':'form-control mb-3'}),
        required = True,
    )