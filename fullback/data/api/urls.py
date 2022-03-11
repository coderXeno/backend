from django import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TodoAPI

urlpatterns = [
    path('todoapi/',TodoAPI.as_view()),
    path('todoapi/<int:pk>',TodoAPI.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)