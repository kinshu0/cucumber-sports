from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index_view, name='events'),
    path('<int:event_id>/', views.specific_event, name='specific-event'),
    path('<int:event_id>/register/', views.event_register, name='specific-event-register'),
    path('<int:event_id>/edit/', views.edit_event, name='edit-event'),

    path('<int:event_id>/add-result/', views.add_result, name='add-result'),
    # path('<int:event_id>/organizer-add-result/', views.organizer_add_result, name='organizer-add-result'),

    # path('<int:event_id>/result/', views.event_result, name='specific-event-result'),
    path('create/', views.create_event, name='create-event'),
]
