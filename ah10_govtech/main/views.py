from __future__ import unicode_literals
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
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm
from .models import SourceUrl, Event, LookingFor, Location


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        location = Location(name=form.cleaned_data.get('location'))
        location.save()
        user.userprofile.location = location
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signuppage.html', {'form': form})


class AddEvent(CreateView):
    form_class = UserCreationForm
    template_name = 'create_event.html'

    def get_success_url(self):
        return reverse('home')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(event_location=self.request.user.userprofile.location)[:4]
        context['friendships'] = LookingFor.objects.filter(location=self.request.user.userprofile.location)[:3]
        context['feeds'] = self.get_feeds()
        return context

    def get_feeds(self):
        feed_urls = SourceUrl.objects.filter(location=self.request.user.userprofile.location)[:3]
        all_feeds = list()
        for url in feed_urls:
            single_feeds = feedparser.parse(url.url)
            all_feeds.extend(single_feeds.entries[:2])
        return random.sample(all_feeds, len(all_feeds))[:3]


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
