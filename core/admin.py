from django.contrib import admin
from core.models import Sermon, Event, Live

class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class LiveAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Sermon, SermonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Live, LiveAdmin)