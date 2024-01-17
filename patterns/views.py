from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Pattern, Comment
from .forms import CommentForm


class PatternList(generic.ListView):
    model = Pattern
    queryset = Pattern.objects.filter(status=1).order_by('-created_on')
    template_name = "pattern_list.html"


class PatternPage(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Pattern.objects.filter(status=1)
        pattern = get_object_or_404(queryset, slug=slug)
        comments = pattern.comments.order_by(
            "-created_on").filter(approved=True)
        saved = False
        if pattern.saved.filter(id=self.request.user.id).exists():
            saved = True
        context = {
            "pattern": pattern,
            "saved": saved,
            "comments": comments,
            "commented": False,
            "comment_form": CommentForm()
        }
        return render(request, "pattern.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Pattern.objects.filter(status=1)
        pattern = get_object_or_404(queryset, slug=slug)
        comments = pattern.comments.order_by(
            "-created_on").filter(approved=True)
        saved = False
        if pattern.saved.filter(id=self.request.user.id).exists():
            saved = True
        context = {
            "pattern": pattern,
            "saved": saved,
            "comments": comments,
            "commented": True,
            "comment_form": CommentForm()
        }

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.pattern = pattern
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, "pattern.html", context)


class SavePattern(View):
    def post(self, request, slug):
        pattern = get_object_or_404(Pattern, slug=slug)
        if pattern.saved.filter(id=request.user.id).exists:
            pattern.saved.remove(request.user)
        else:
            pattern.saved.add(request.user)
        return HttpResponseRedirect(reverse('pattern_page', args=[slug]))


class EditComment(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'
    success_message = 'Your comment has been edited successfully and is now pending approval.'
    success_url = '/'


class DeleteComment(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'delete_comment.html'
    success_message = 'Your comment has been deleted successfully.'
    success_url = '/'
