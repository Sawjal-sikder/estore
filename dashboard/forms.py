from django import forms
from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['mobile_no'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
        self.fields['shipping_address'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Shipping address'})
        self.fields['shipping_mobile'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Shipping Mobile No'})
