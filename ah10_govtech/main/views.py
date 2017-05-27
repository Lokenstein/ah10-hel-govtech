from django.http import HttpResponse
from django.views.generic import ListView
from models import SourceUrl

class RSSList(ListView):
    model = SourceUrl
