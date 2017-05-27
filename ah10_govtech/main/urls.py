from django.conf.urls import url
from views import RSSList

from . import views

urlpatterns = [
    url(r'^$', RSSList.as_view()),
]

