from django.urls import path
from core.views import index, about, sermon, event, contact

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('sermons', sermon, name='sermon'),
    path('events', event, name='event'),
    path('contact', contact, name='contact'),
]