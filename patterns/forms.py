from .models import Pattern, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        widgets = {
            'description': SummernoteWidget(),
            'abbreviations': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }
        fields = [
            'title',
            'featured_image',
            'description',
            'difficulty_level',
            'yarn_type',
            'hook_size',
            'gauge',
            'abbreviations',
            'instructions',
            'status',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)