from . import views
from django.urls import path

urlpatterns = [
    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('pattern/<slug:slug>/', views.PatternPage.as_view(), name='pattern_page'),
    path(
        '<slug:slug>/saved/', views.SavePattern.as_view(), name='save_pattern'
    ),
    path('pattern/<int:pk>/edit_comment/',
         views.EditComment.as_view(), name='edit_comment'),
    path('pattern/<int:pk>/delete_comment/',
         views.DeleteComment.as_view(), name='delete_comment'),
]
