"""yowft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Rascunhos ---
Funcionou na forma abaixo
path('cadastro.json', TemplateView.as_view(template_name="cadastro.json"), name='cadastro.json'),
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('imginicial', TemplateView.as_view(template_name="tstpedido/T9e10Imageminicial1.html"), name='imginicial'),
    path('dadoslogin', views.dadoslogin, name='dadoslogin'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('amigos', TemplateView.as_view(template_name="tstpedido/Amigos.html"), name='amigos'),
    path('carregajson', TemplateView.as_view(template_name="dados.json"), name='carregajson'),
              ]
