from django import forms
from .models import Hospital, Tecnico, Pedido, Resposta


class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'nif', 'state', 'hospital', 'password']
        widgets = {
            'email': forms.EmailInput()
        }


class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'nif', 'state', 'compname', 'password']
        widgets = {
            'email': forms.EmailInput()
        }

