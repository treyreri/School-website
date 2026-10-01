from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import RegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return '/profile/'  


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'