from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pattern, Comment
from .forms import PatternForm, CommentForm


class PatternList(generic.ListView):
    """
    Displays a list of published crochet patterns.
    Filters them from newest to oldest.
    """
    model = Pattern
    queryset = Pattern.objects.filter(status=1).order_by('-created_on')
    template_name = "pattern_list.html"
    paginate_by = 9


class PatternPage(View):
    """
    Displays the pattern details.
    """

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
            messages.success(self.request, 'Your comment is pending approval.')
        else:
            comment_form = CommentForm()

        return render(request, "pattern.html", context)


class CreatePattern(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Allows authenticated users to create crochet patterns
    from the UI.
    """
    model = Pattern
    form_class = PatternForm
    template_name = 'create_pattern.html'
    success_url = '/'
    success_message = 'Pattern has been created successfully.'

    def form_valid(self, form):
        """
        If the form is valid, the author is set to
        the authenticated user and the title is
        populated as the slug
        """
        form.instance.created_by = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class EditPattern(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Allows authenticated users to edit their own patterns.
    """
    model = Pattern
    form_class = PatternForm
    template_name = 'edit_pattern.html'
    success_url = '/'
    success_message = 'Pattern has been edited successfully.'

    def form_valid(self, form):
        """
        Sets the author of the pattern to the authenticated
        user if the form is valid.
        """
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        """
        Prevents users from editing patterns they have not
        created.
        Written with help from Stack Overflow
        (link in README.md)
        """
        queryset = super(EditPattern, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user)
        return queryset


class DeletePattern(LoginRequiredMixin, DeleteView):
    """
    Allows authenticated users to delete their own patterns.
    """
    model = Pattern
    form_class = PatternForm
    template_name = 'delete_pattern.html'
    success_url = '/'
    success_message = 'Pattern has been deleted.'

    def get_queryset(self):
        """
        Prevents users from deleting patterns they have not
        created.
        Written with help from Stack Overflow
        (link in README.md)
        """
        queryset = super(DeletePattern, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user)
        return queryset

    def delete(self, request, *args, **kwargs):
        """
        Retrieves the success message as the SuccessMessageMixin
        is not compatible with DeleteView.
        Solution found on Stack Overflow
        """
        messages.success(self.request, self.success_message)
        return super(DeletePattern, self).delete(request, *args, **kwargs)


class EditComment(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Allows authenticated users to edit their own comments.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'
    success_url = '/'
    success_message = 'Comment has been edited and is now pending approval.'

    def form_valid(self, form):
        """
        Sets the author of the comment to the user if the form
        is valid.
        Reverts the approved status to false.
        """
        form.instance.author = self.request.user
        self.object.approved = False
        self.object.save()
        return super().form_valid(form)

    def get_queryset(self):
        """
        Prevents users from editing patterns they have not
        created.
        Written with help from Stack Overflow
        (link in README.md)
        """
        queryset = super(EditComment, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class DeleteComment(LoginRequiredMixin, DeleteView):
    """
    Allows authenticated users to delete their own comments.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'delete_comment.html'
    success_url = '/'
    success_message = 'Comment has been deleted successfully.'

    def get_queryset(self):
        """
        Prevents users from deleting comments they have not
        created.
        Written with help from Stack Overflow
        (link in README.md)
        """
        queryset = super(DeleteComment, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def delete(self, request, *args, **kwargs):
        """
        Retrieves the success message as the SuccessMessageMixin
        is not compatible with DeleteView.
        Solution found on Stack Overflow
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)


class SavePattern(LoginRequiredMixin, View):
    """
    Allows authenticated users to save patterns for later.
    """

    def post(self, request, slug):
        pattern = get_object_or_404(Pattern, slug=slug)
        if pattern.saved.filter(id=request.user.id).exists():
            pattern.saved.remove(request.user)
            messages.success(
                self.request, 'Pattern removed from My Saved Patterns.'
            )
        else:
            pattern.saved.add(request.user)
            messages.success(
                self.request, 'Pattern added to My Saved Patterns.'
            )
        return HttpResponseRedirect(reverse('pattern_page', args=[slug]))


class SavedPatternList(LoginRequiredMixin, generic.ListView):
    """
    Displays the authenticated user's saved patterns.
    """
    model = Pattern
    template_name = "saved_pattern_list.html"
    paginate_by = 9
    """
    Retrieves the patterns saved by the authenticated user.
    """

    def get_queryset(self):
        return Pattern.objects.filter(saved=self.request.user.id)
