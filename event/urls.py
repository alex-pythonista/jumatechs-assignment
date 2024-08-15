from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.event_details, name='event-details'),
]