#LOS FORMULARIOS DE DJANGO SON CLASES

from django import forms


class FormularioEmpleados(forms.Form):

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT

    nombres=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        # max_length=50
    )

    apellidos=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=False,
        # max_length=50
    )

    foto=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        # max_length=200
    )

    cargo=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True
    )
    
    salario=forms.ChoiceField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True
    )

    contacto=forms.ChoiceField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        # max_length=20
    )