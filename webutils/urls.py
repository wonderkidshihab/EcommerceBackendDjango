from django.urls import include, path
from .views import StoryView, StoryDetailView
urlpatterns = [
    path('', StoryView.as_view(), name="Story"),
    path('<int:pk>/', StoryDetailView.as_view(), name="Story_detail"),
]
