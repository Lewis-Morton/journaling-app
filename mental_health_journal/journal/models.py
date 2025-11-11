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
    

    
class Conversation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='participants')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'conversation']


class ChatMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
