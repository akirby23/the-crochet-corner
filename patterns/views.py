from django.shortcuts import render
from django.views import generic
from .models import Pattern


class PatternList(generic.ListView):
    model = Pattern
    queryset = Pattern.objects.filter(status=1).order_by('-created_on')
    template_name = index.html



