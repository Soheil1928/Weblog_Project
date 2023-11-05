from typing import Any
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .forms import RegisterForm, EditRegisterForm, CreateProfileForm, ChangePasswordForm
from django.views import generic
from django.urls import reverse_lazy
from blog_app.models import Profile


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditRegisterView(generic.UpdateView):
    form_class = EditRegisterForm
    template_name = 'registration/edit_register.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')


class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        context['profile'] = profile
        return context


class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('home')