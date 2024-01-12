from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Pattern
from .forms import CommentForm


def home(request):
    return render(request, 'index.html')


class PatternList(generic.ListView):
    model = Pattern
    queryset = Pattern.objects.filter(status=1).order_by('-created_on')
    template_name = "pattern_list.html"


class PatternPage(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Pattern.objects.filter(status=1)
        pattern = get_object_or_404(queryset, slug=slug)
        context = {
            "pattern": pattern,
            "comment_form": CommentForm()
        }
        return render(request, "pattern.html", context)
