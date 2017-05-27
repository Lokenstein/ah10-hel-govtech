from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import ListView
from models import SourceUrl
from django.shortcuts import render

class RSSList(ListView):
    model = SourceUrl
