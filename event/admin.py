from django.contrib import admin

from .models import Event, Attendee

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'location', 'host', 'seats')
    list_filter = ('datetime', 'location', 'host')
    search_fields = ('title',)


admin.site.register(Attendee)