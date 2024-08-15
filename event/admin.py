from django.contrib import admin

from .models import Event, Attendee

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'seats', 'available_seats')
    list_filter = ('datetime',)
    search_fields = ('title',)


admin.site.register(Attendee)