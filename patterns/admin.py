from django.contrib import admin
from .models import Pattern
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pattern)
class PatternAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'instructions', 'abbreviations')
