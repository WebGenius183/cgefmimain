from django.contrib import admin
from core.models import Sermon, Event, Live, Gallery, GalleryImage

class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class LiveAdmin(admin.ModelAdmin):
    list_display = ['title']

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

admin.site.register(Sermon, SermonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Live, LiveAdmin)