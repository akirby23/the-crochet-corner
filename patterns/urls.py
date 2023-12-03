from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('<slug:slug>/', views.PatternPage.as_view(), name='pattern_page')
]
