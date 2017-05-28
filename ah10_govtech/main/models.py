# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SourceUrl(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    lastVisited = models.DateTimeField(auto_now=True)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, blank=True)
    event_date = models.DateTimeField(auto_now_add=True, editable=False)
    event_category = models.ForeignKey(Category, on_delete=models.SET("Category_deleted"))
    # event_location_longitude = models.DecimalField(max_digits=9, decimal_places=5)
    # event_location_latitude = models.DecimalField(max_digits=9, decimal_places=5)
    event_location = models.TextField(max_length=1000)
    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name


class LookingFor(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name





