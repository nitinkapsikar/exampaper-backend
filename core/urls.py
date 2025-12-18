from django.urls import path
from .views import DocumentListAPI

urlpatterns = [
    path('documents/', DocumentListAPI.as_view()),
]
