from django import forms
from .models import MensagemContato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Digite seu nome...',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Digite seu e-mail...',
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Digite sua mensagem...',
            }),
        }