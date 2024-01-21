from . import views
from django.urls import path

urlpatterns = [
    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('saved_patterns/', views.SavedPatternList.as_view(),
         name='saved_pattern_list'),
    path('patterns/<slug:slug>/', views.PatternPage.as_view(),
         name='pattern_page'),
    path('create_pattern/', views.CreatePattern.as_view(),
         name='create_pattern'),
    path('patterns/<slug:slug>/edit_pattern/', views.EditPattern.as_view(),
         name='edit_pattern'),
    path('save/pattern/<slug:slug>/', views.SavePattern.as_view(),
         name='save_pattern'),
    path('pattern/<int:pk>/edit_comment/', views.EditComment.as_view(),
         name='edit_comment'),
    path('pattern/<int:pk>/delete_comment/', views.DeleteComment.as_view(),
         name='delete_comment'),
]
