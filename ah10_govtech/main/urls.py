from django.conf.urls import url

from . import views
from .views import HomeView
from .views import CreateEventView
from .views import EventDetailView
from .views import signup

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),# eventlist
    url(r'^create-event/$', CreateEventView.as_view(), name='create-event'),
    url(r'^event/(?P<pk>\d+)$', EventDetailView.as_view(), name='event-detail'),
    url(r'^signup/$', signup, name='signup'),
    #url(r'^question-list/$', QuestionListView.as_view(), name='event-detail'),
]

