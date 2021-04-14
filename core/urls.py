from django.urls import path

from .views import HomeView, formView, classifyView, classifying

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('form/', formView.as_view(), name='form'),
    path('classify/<int:pk>/', classifyView.as_view(), name='classify'),
    path('classifying/<int:pk>/', classifying, name='classifying')
]
