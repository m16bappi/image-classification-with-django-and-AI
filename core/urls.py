from django.urls import path

from .views import HomeView, formView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('form/', formView.as_view(), name='form')
]
