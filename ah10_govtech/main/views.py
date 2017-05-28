from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import ListView
from models import SourceUrl
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

class RSSList(ListView):
    model = SourceUrl


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("login")


def login_view(request):
    user = request.POST['user']
    pwd = request.POST['pwd']
    user = authenticate(request, username=user, password=pwd)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("index")
    else:
        return HttpResponseRedirect("login")