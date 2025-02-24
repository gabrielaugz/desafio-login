# accounts/forms.py
import re
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )

    # verificação do campo email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("O campo E-mail não pode ser vazio.")

        if not User.objects.filter(email=email).exists():
            raise ValidationError("E-mail inexistente") 

        return email

    # verificação do campo senha
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError("O campo Senha não pode ser vazio.")
        return password

    # senha precisa ser igual a registrada
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return cleaned_data

            user_auth = authenticate(username=user.username, password=password)

            if user_auth is None:
                raise ValidationError("Senha inválida")
        return cleaned_data

# formulário de registro
class RegisterForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nome'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Senha'})
    )

    # validação do nome
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', name):
            raise ValidationError("O nome deve conter apenas letras.")
        return name

    # validação da senha
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("A senha deve conter ao menos uma letra maiúscula.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("A senha deve conter ao menos um número.")
        if not re.search(r'[\W_]', password):
            raise ValidationError("A senha deve conter ao menos um caractere especial.")
        return password

    # validação da igualdade das senhas
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Os campos de senha devem ser idênticos.")
        return cleaned_data