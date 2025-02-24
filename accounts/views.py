# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, RegisterForm

# validação do email e senha. se não forem válidos, emite mensagem de erro
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user_obj = User.objects.get(email=email)
            user = authenticate(username=user_obj.username, password=password)

            if user:
                login(request, user)
                return redirect('menu') 
            else:
                messages.error(request, "Não foi possível autenticar.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# valida os campos no forms. cria usuário no BD e realiza o login de forma automática
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=email,
                first_name=name,
                email=email,
                password=password
            )
            # login automático
            login(request, user)
            return redirect('menu')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def menu_view(request):
    return render(request, 'menu.html')