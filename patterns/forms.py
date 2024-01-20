from .models import Pattern, Comment
from django import forms



class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = [
            
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
