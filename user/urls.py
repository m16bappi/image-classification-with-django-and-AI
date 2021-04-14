from django.urls import path
from .views import registerView, loginView, logoutView

urlpatterns = [
    path('register/', registerView.as_view(), name='register'),
    path('login/', loginView.as_view(), name='login'),
    path('logout/', logoutView, name='logout')
]
