from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignUpForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user 
    


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ["bio","city", "birth_date"]

    # def __init__(self, *args, **kwargs):
    #     super(ProfileEditForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']
        # exclude = ['password','user']
    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})