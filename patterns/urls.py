from . import views
from django.urls import path

urlpatterns = [
    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('<slug:slug>/', views.PatternPage.as_view(), name='pattern_page'),
    path('saved/<slug:slug>', views.SavePattern.as_view(), name='save_pattern'),
]
