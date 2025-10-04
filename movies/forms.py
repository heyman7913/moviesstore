from django import forms
from .models import Petition

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['title', 'movie_name', 'director', 'year', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Petition Title'}),
            'movie_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Director (optional)'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year (optional)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Why should this movie be added?'}),
        }
