from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class JournalEntry(models.Model):
    MOOD_CHOICES = [('content', 'Content'),
                     ('melancholy', 'Melancholy'), 
                     ('sorrowful', 'Sorrowful'),
                     ('grateful', 'Grateful'),
                     ('energetic', 'Energetic'),
                     ('positive', 'Positive'),
                     ('motivated', 'Motivated'),
                     ('tired', 'Tired'),
                     ('depressive', 'Depressive')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    







