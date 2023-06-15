
from django.db import models

class Note(models.Model):
    NOTE_TYPES = [
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
