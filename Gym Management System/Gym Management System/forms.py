from django import forms
from django.forms.widgets import PasswordInput
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm ,UserChangeForm
import uuid

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    gym_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["full_name", "password1", "password2", "email", "gym_name"]

    def save(self,commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = uuid.uuid4().hex[:30]
        user.email = self.cleaned_data.get('email')
        
        if commit:
            user = user.save()
        return user 

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('gym_name','full_name')
    
#     def save(self,commit=True):
#         user.gym_name = self.cleaned_data.get('gym_name')
#         user.full_name = self.cleaned_data.get('full_name')


class LoginForm(UserChangeForm):    
    class Meta:
        model = User
        fields = ('username','email')

