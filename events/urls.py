from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index_view, name='events'),
    path('<int:event_id>', views.specific_event, name='specific-event'),
    path('<int:event_id>/register', views.event_register, name='specific-event-register')
]
