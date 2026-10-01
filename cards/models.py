from django.db import models

# Create your models here.

class Deck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.description}"

class Flashcard(models.Model):
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name="flashcards"
    )
    front = models.CharField(max_length=255)
    back = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.front}, {self.back}"