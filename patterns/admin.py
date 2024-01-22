from django.contrib import admin
from .models import Pattern, Comment
from django_summernote.admin import SummernoteModelAdmin

"""
Prepopulates the slug field with the pattern title.
Sets the summernote fields.
Written with help from the 'I Think Therefore I Blog' walkthrough.
"""


@admin.register(Pattern)
class PatternAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'instructions', 'abbreviations')


"""
Displays comments and adds filter options.
Allows the site admin to approve comments.
Written with help from the 'I Think Therefore I Blog' walkthrough.
"""


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'author', 'text', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'author')
    actions = ['approve_comment', 'disapprove_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_comment(self, request, queryset):
        queryset.update(approved=False)