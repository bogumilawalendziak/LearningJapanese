from django.db import models


class Word(models.Model):
    word = models.TextField()
    definition = models.TextField()
    example = models.TextField()
    translation = models.TextField()
    pronunciation = models.TextField()
    created = models.DateField(auto_now_add=True)
