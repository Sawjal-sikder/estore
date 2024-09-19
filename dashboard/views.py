from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from accounts.models import Profile
from .forms import ProfileForm


# Create your views here.
class profileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'dashboard/my-account.html'
    success_url = reverse_lazy("profile_update")

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context
