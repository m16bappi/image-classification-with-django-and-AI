from os import listdir

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .character_recognition.character_extractor import CharacterExtractor
from .forms import imageUploadForm
from .models import imageExtractor, classifiedCharacters, imageWithCharacter


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
        object.character_extractor(path=form.cleaned_data['image'])

        imList = listdir(path='media')
        for image in imList:
            object = imageExtractor.objects.create(image=image)
            object.save()
        return redirect('/')


class classifyView(LoginRequiredMixin, DetailView):
    model = imageExtractor
    template_name = 'core/Classified.html'

    def get_context_data(self, **kwargs):
        context = super(classifyView, self).get_context_data()
        context['classified_context'] = classifiedCharacters.objects.all().distinct()
        return context


def classifying(request, pk):
    if request.method == 'POST':
        data = request.POST
        object = imageExtractor.objects.get(pk=pk)
        if not object.voted.filter(id=request.user.id).exists():
            object.voted.add(request.user)
            value = imageWithCharacter.objects.create(image_id=pk, character_id=data['radio'])
            value.save()

            list = []
            classify = object.imagewithcharacter_set.all()
            if object.voted.count() > 3:
                pass

    return redirect('/')


def classified(request):
    pass
