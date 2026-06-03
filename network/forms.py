# forms.py
from django import forms
from .models import posts

class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'style': 'width: 95%; margin-top: 10px;margin-right:40px;'}),  # Customize the textarea attributes
        }
        labels = {
            'body': 'Write a post',  # Add a label for the body field
        }
