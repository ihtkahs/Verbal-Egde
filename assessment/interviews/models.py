from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    is_candidate = models.BooleanField(default=True)  # To differentiate user roles (if needed)

    def __str__(self):
        return self.user.username
    
class Question(models.Model):
    CATEGORY_CHOICES = [
        ('HR', 'HR Interview'),
        ('TECHNICAL', 'Technical Interview'),
        ('GENERAL', 'General Communication'),
    ]
    
    question_text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.IntegerField(default=1)  # 1 (Easy), 2 (Medium), 3 (Hard)

    def __str__(self):
        return self.question_text


class AudioResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio_responses/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text[:30]}"
