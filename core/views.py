from os import listdir

from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .character_recognition.character_extractor import CharacterExtractor
from .forms import imageUploadForm
from .models import imageExtractor, classifiedCharacters, imageWithCharacter, classifiedImage


class HomeView(TemplateView):
    template_name = 'core/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['objects'] = imageExtractor.objects.filter(status=False)
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
    template_name = 'core/Details.html'

    def get_context_data(self, **kwargs):
        context = super(classifyView, self).get_context_data()
        context['classified_context'] = classifiedCharacters.objects.all().distinct()
        return context


def classifying(request, pk):
    if request.method == 'POST':
        post = request.POST
        object = imageExtractor.objects.get(pk=pk)
        if not object.voted.filter(id=request.user.id).exists():
            object.voted.add(request.user)
            value = imageWithCharacter.objects.create(image_id=pk, character_id=post['radio'])
            value.save()

        data = object.imagewithcharacter_set.values('character_id').annotate(count=Count('character_id')). \
            filter(count__gt=3)
        for v in data:
            object.status = True
            object.save()
            classify = classifiedImage.objects.create(classified_char_id=v['character_id'], image=object,
                                                      percentage=(v['count']*100)//object.voted.count())
            classify.save()

    return redirect('/')


class classified(TemplateView):
    template_name = "core/Classified.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['objects'] = classifiedImage.objects.all()
        return context
