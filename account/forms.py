from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="Nombre")
    last_name = forms.CharField(max_length=30, label="Apellido")
    email = forms.EmailField(max_length=254, label="Correo Electrónico", help_text='Required. Inform a valid email address.')
    telefono = forms.CharField(max_length=15, label="Teléfono")
    direccion = forms.CharField(max_length=255, label="Dirección")
    tipo = forms.ChoiceField(choices=Perfil.USUARIO_TIPO_CHOICES, label="Tipo de Usuario")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'telefono', 'direccion', 'tipo')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            perfil = Perfil.objects.create(usuario=user, telefono=self.cleaned_data['telefono'], direccion=self.cleaned_data['direccion'], tipo=self.cleaned_data['tipo'])
        return user

class PerfilForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Perfil
        fields = ('telefono', 'direccion', 'tipo')

