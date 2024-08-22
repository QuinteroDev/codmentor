from django.db import models

class Exercise(models.Model):
    language = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    prompt = models.TextField()
    exercise_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.language.capitalize()} ({self.difficulty})"