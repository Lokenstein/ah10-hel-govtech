from __future__ import unicode_literals
from django.http import HttpResponse
import feedparser, random
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

# models import
from models import SourceUrl #?
from .models import SourceUrl, Event, LookingFor

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


class AddEvent(CreateView):
    form_class = UserCreationForm
    template_name = 'create_event.html'

    def get_success_url(self):
        return reverse('home')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()[:4]
        context['friendships'] = LookingFor.objects.all()[:4]
        context['feeds'] = self.get_feeds()
        return context

    def get_feeds(self):
        feed_urls = SourceUrl.objects.all()[:2]
        all_feeds = list()
        for url in feed_urls:
            single_feeds = feedparser.parse(url.url)
            all_feeds.extend(single_feeds.entries[:2])
        #for url in feed_urls:
        #feeds = feedparser.parse("http://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss")
        return random.sample(all_feeds, 3)


class NewSubmissionView(CreateView):
    model = SourceUrl
    fields = (
        'title', 'url'
    )

    template_name = 'new_submission.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewSubmissionView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        new_link = form.save(commit=False)
        new_link.submitted_by = self.request.user
        new_link.save()

        self.object = new_link
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')


class CreateEventView(CreateView):
    model = Event
    fields = ('name','description','event_date','location')
    template_name = 'create_event.html'

    def form_valid(self,form):
        new_event=form.save(commit=False)
        new_event


class EventDetailView(DetailView):
    model = Event
