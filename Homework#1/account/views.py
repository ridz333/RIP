from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User


class AccountRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('account:edit')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result


class AboutProfileView(View, LoginRequiredMixin):
    template_name = 'profile/about.html'

    def get(self,request, username, *args, **kwargs):
        return render(request, self.template_name, {
            'user': User.objects.get(username=username),
            'title': 'Блог | Профиль',
            'page': 'profile'
        })


class EditProfileView(View, LoginRequiredMixin):
    template_name = 'profile/edit.html'

    def get(self,request, *args, **kwargs):
        user = UserForm(instance=request.user)
        profile = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {
            'user_form': user,
            'profile_form': profile,
            'title': 'Блог | Изменить'
        })

    def post(self,request, *args, **kwargs):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account:about', request.user.username)