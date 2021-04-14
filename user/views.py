from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import register, loginForm


class registerView(FormView):
    form_class = register
    template_name = 'user/Register.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


class loginView(FormView):
    form_class = loginForm
    template_name = 'user/Login.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request=self.request, user=user)
            return redirect('home')
        else:
            return redirect('login')


def logoutView(request):
    logout(request)
    return redirect('/')
