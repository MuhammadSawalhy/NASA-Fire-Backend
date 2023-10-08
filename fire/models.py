from django.db import models

class Fire(models.Model):
    confirmed = models.BooleanField(default=True)
    location = models.JSONField()
    start_time = models.DateTimeField()
    danger = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    images = models.JSONField(default=list)  # Storing image URLs as a list

    def __str__(self):
        return f"Fire at {self.location} - Start Time: {self.start_time}"
