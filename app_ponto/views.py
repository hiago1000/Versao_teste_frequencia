from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_sucesso(request):
    return render(request, 'app_ponto/login_sucesso.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=['username'],
                   password=['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(login_sucesso) #importa o redirect em django.shorcuts e só chamar a função.
                else:
                    return HttpResponse('Conta desativada')
            else:
                return HttpResponse('Conta inválida')
    else:
        form = LoginForm()
    return render(request, 'app_ponto/login.html', {'form': form})

