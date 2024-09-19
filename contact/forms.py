from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['subject'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'})
        self.fields['message'].widget = forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 3})
