from django.contrib import admin
from .models import Pattern
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pattern)
class PatternAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'instructions')
