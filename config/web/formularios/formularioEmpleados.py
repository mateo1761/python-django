from django import forms

class FormularioEmpleados(forms.Form):

    CARGOS = (
        (0, '---'),
        (1, 'Chef'),
        (2, 'Administrador'),
        (3, 'Mesero'),
        (4, 'Ayudante chef')
    )

    nombre = forms.CharField(
        required = True,
        max_length = 250,
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    apellido = forms.CharField(
        required = True,
        max_length = 250,
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    fotografia = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    cargo = forms.ChoiceField(
        required = True,
        widget = forms.Select(attrs={'class': 'form-control mb-3'}),
        choices = CARGOS
    )
    Salario = forms.CharField(
        required = True,
        max_length = 20,
        widget = forms.NumberInput(attrs={'class': 'form-control mb-3'})
    )
    contacto = forms.CharField(
        required = True,
        max_length = 250,
        widget = forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
