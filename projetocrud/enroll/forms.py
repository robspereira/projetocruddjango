from django.core import validators
from django import forms 
from .models import Usuario 

class CadastroEstudante(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['codigo', 'nome', 'email', 'curso', 'senha']
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'curso': forms.TextInput(attrs={'class':'form-control'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].required=True
        self.fields['codigo'].error_messages['required'] = 'O código é obrigatório!'
        self.fields['nome'].required=True
        self.fields['nome'].error_messages['required'] = 'Nome não pode ficar em branco!'
        self.fields['email'].required=True
        self.fields['email'].error_messages['required'] = 'Email não pode ficar em branco!'
        self.fields['curso'].required=True
        self.fields['curso'].error_messages['required'] = 'Curso não pode ficar em branco!'
        self.fields['senha'].required=True
        self.fields['senha'].error_messages['required'] = 'Senha não pode ficar em branco!'

class AtualizarCadastroEstudante(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['codigo', 'nome', 'email', 'curso']
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'curso': forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].required=True
        self.fields['codigo'].error_messages['required'] = 'O código é obrigatório!'
        self.fields['nome'].required=True
        self.fields['nome'].error_messages['required'] = 'Nome não pode ficar em branco!'
        self.fields['email'].required=True
        self.fields['email'].error_messages['required'] = 'Email não pode ficar em branco!'
        self.fields['curso'].required=True
        self.fields['curso'].error_messages['required'] = 'Curso não pode ficar em branco!'
