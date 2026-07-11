from django.urls import path

from .views import CreatePostView

urlpatterns = [
    path("posts/",CreatePostView.as_view(),name="create_post",),
]
