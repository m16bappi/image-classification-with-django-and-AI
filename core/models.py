from django.db import models


class imageExtractor(models.Model):
    image = models.ImageField()

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
