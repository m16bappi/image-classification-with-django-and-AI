from django.contrib import admin

from .models import imageExtractor, classifiedCharacters, classifiedImage, imageWithCharacter


admin.site.register(imageExtractor)
admin.site.register(classifiedImage)
admin.site.register(classifiedCharacters)
admin.site.register(imageWithCharacter)
