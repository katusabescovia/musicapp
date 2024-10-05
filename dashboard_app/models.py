from django.db import models

class Search(models.Model):
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search by {self.artist_name or 'Unknown Artist'}"

