# -*- coding: utf-8 -*-
from django.views.generic import CreateView,TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib import messages # Metodo para la validacion de los campos
from apps.login.forms import LoginForm, UserForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from .models import PerfilesUsuario
from django.contrib.auth.models import User, Group
from django.db import connection, transaction # Cursor de django
from passlib.hash import django_pbkdf2_sha256 as handler # Proceso para encriptar las contrasena
import hashlib

import time

def base_view(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/cantidad')
            
