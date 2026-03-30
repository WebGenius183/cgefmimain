from django.db import models
import re

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    date = models.DateField()

    def get_youtube_id(self):
        patterns = [
            r"v=([a-zA-Z0-9_-]+)",
            r"youtu\.be/([a-zA-Z0-9_-]+)",
            r"live/([a-zA-Z0-9_-]+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, self.link)
            if match:
                return match.group(1)
        return None

    def thumbnail(self):
        vid = self.get_youtube_id()
        if vid:
            return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"
        return ""

class Event(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=100)
    image = models.ImageField( upload_to="events")
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
class Live(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=10000)
    link = models.TextField()
    
    def __str__(self):
        return self.link