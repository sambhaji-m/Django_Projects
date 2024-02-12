# In your_app/forms.py

from django import forms
from .models import enquiry

class EnquiryForm(forms.ModelForm):
    SUBJECT_CHOICES = [
        ('Job Opening', 'Job Opening'),
        ('Current Project', 'Current Project'),
        ('Hire Developer', 'Hire Developer'),
    ]
    
    subject_type = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

 
    class Meta:
        model = enquiry
        fields = ['name', 'subject_type', 'email', 'mobile_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'subject_type': forms.Select(attrs={'class': 'form-control'  }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 8,'placeholder': 'Enter your message', 'style': 'width: 100%;'}),
        }

