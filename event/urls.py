from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.event_details, name='event-details'),
    path('my-events/', views.my_event, name='my-events'),
    path('register/<int:id>/', views.register, name='register'),
    path('unregister/<int:id>/', views.unregister, name='unregister'),
]