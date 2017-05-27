from django.contrib import admin
from .models import SourceUrl, UserProfile, Category, Location, LookingFor, Event
 
admin.site.register(SourceUrl)
admin.site.register(Event)
admin.site.register(LookingFor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(UserProfile)
