from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'full_name', 'email', 'phone',
            'linkedin_url', 'portfolio_url',
            'resume', 'cover_letter'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn profile URL'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Portfolio URL'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your cover letter'}),
        }
