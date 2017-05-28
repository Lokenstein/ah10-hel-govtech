"""ah10_govtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.views import login, logout
from ah10_govtech.views import HomeView
from ah10_govtech.views import CreateEventView
from ah10_govtech.views import EventDetailView
from ah10_govtech.views import QuestionListView


admin.autodiscover()

urlpatterns = [
    url(r'^main/', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
     url(r'^$', HomeView.as_view(), name='home'),# eventlist
    url(r'^create-event/$', CreateEventView.as_view(), name='create-event'),
    url(r'^event-detail/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^question-list/$', QuestionListView.as_view(), name='event-detail'),

     
]
