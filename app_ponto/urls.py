from django.urls import path
from django.contrib.auth import views as auth_views
from app_ponto.views import user_login,login_sucesso

from . import views


urlpatterns=[
    path('login/sucesso/',login_sucesso, name='login_sucesso'),
    path('',user_login,name="login"),
    path('login/',user_login,name='login'),

]