from django.urls import path

from .views import HomeView, formView, classifyView, classifying, classified

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('form/', formView.as_view(), name='form'),
    path('classifying/<int:pk>/', classifying, name='classifying'),
    path('classify/<int:pk>/', classifyView.as_view(), name='classify'),
    path('classified', classified.as_view(), name='classified')
]
