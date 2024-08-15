from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=100)
    seats = models.IntegerField()
    thumbnail = models.ImageField(upload_to='event_thumbnails', blank=True, null=True)

    def __str__(self):
        return f"💫{self.title } | 📍Location: {self.location}"
    
    def available_seats(self):
        return self.seats - self.attendees.count()
    

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} attending {self.event.title}"