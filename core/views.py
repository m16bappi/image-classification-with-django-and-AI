from os import listdir

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .character_recognition.character_extractor import CharacterExtractor
from .forms import imageUploadForm
from .models import imageExtractor


class HomeView(TemplateView):
    template_name = 'core/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['objects'] = imageExtractor.objects.all()
        return context


class formView(FormView):
    form_class = imageUploadForm
    template_name = 'core/Form.html'

    def form_valid(self, form):
        object = CharacterExtractor()
        # #object.character_extractor(path=form.cleaned_data['image'])
        #
        # imList = listdir(path='media')
        # for image in imList:
        #     object = imageExtractor.objects.create(image=image)
        #     object.save()
        return redirect('/')
