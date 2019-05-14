from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_sucesso(request):
    return render(request, 'app_ponto/login_sucesso.html')

def user_login(request):
    if request.method == "POST":

        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('Senha')
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(login_sucesso)
            else:
                return HttpResponse("Usuário desativado")
                # Retorna uma mensagem de erro de 'conta desabilitada' .
        else:
            return HttpResponse("Login ou senha inválido")

            # Retorna uma mensagem de erro 'login inválido'.
    else:
        form = LoginForm()
    return render(request, 'app_ponto/login.html', {'form': form})
