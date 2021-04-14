from django.db import models
from django.contrib.auth.models import User


class imageExtractor(models.Model):
    image = models.ImageField()
    voted = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.image.name


class classifiedImage(models.Model):
    classified_char = models.CharField(max_length=10)
    image = models.ImageField()

    def __str__(self):
        return self.classified_char


class classifiedCharacters(models.Model):
    characters = models.CharField(max_length=10)

    def __str__(self):
        return self.characters


class imageWithCharacter(models.Model):
    image = models.ForeignKey(imageExtractor, on_delete=models.CASCADE)
    character = models.ForeignKey(classifiedCharacters, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.image.name
