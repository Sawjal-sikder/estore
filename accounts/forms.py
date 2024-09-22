from django import forms
from django.contrib.auth.models import User  # Assuming you are using the built-in User model


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
        max_length=55,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        max_length=55,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

    class Meta:
        model = User  # Specify the model here
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)
