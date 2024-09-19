from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Create your views here.


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Profiles'] = CompanyProfile.objects.filter(is_active=True)
        return context
