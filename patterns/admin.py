from django.contrib import admin
from .models import Pattern, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pattern)
class PatternAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'instructions', 'abbreviations')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'author', 'text', 'created_on')
    list_filter = ('author', 'created_on')
