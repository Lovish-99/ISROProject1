from django.contrib import admin
from django.urls import path
from map import views as map_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',map_views.home, name='home'),
    path('contact/', map_views.contact, name='contact'),
    path('services/', map_views.services, name='services'),
    path('feedback/', map_views.feedback, name='feedback'),
    path('about/', map_views.about, name='about')
]
