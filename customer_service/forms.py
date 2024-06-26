from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ServiceRequest

# Form for the registration page
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for submitting the service request
class ServiceRequestForm(forms.ModelForm):
    request_type = forms.ChoiceField(choices=ServiceRequest.REQUEST_TYPE_CHOICES)
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachments']

    # Function used to adjust the size of description box
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 50}) 