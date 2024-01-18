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
    """
    Allows the user to save the pattern for later.
    """

    def post(self, request, slug):
        pattern = get_object_or_404(Pattern, slug=slug)
        if pattern.saved.filter(id=request.user.id).exists():
            pattern.saved.remove(request.user)
            messages.success(
                self.request, 'This pattern has been removed from My Saved Patterns.'
            )
        else:
            pattern.saved.add(request.user)
            messages.success(
                self.request, 'This pattern has been added to My Saved Patterns.'
            )
        return HttpResponseRedirect(reverse('pattern_page', args=[slug]))


class SavedPatternList(generic.ListView):
    model = Pattern
    template_name = "saved_pattern_list.html"
    """
    Retrieves the patterns saved by the authenticated user.
    """
    def get_queryset(self):
        return Pattern.objects.filter(saved=self.request.user.id)


class EditComment(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'
    success_message = 'Your comment has been edited and is now pending approval.'
    success_url = '/'

    def form_valid(self, form):
        """
        Sets the author of the comment to the user if the form
        is valid.
        Reverts the approved status to false.
        """
        form.instance.name = self.request.user
        self.object.approved = False
        self.object.save()
        return super().form_valid(form)


class DeleteComment(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'delete_comment.html'
    success_message = 'Your comment has been deleted successfully.'
    success_url = '/'
