from django import forms
from . models import Apply ,Job
class Form(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'coverletter']
    
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'website': forms.URLInput(attrs={'class': 'form-control'}),
        #     'cv': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        #     'coverletter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        # }


class PostJob(forms.ModelForm):
    class Meta:
        model = Job
        fields ="__all__"
        exclude = ['slug','user']  # Exclude slug field from the form