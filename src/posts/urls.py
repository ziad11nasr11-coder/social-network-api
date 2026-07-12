from django.urls import path

from .views import CreatePostView, PostListView,

urlpatterns = [
    path(
        "posts/",
        PostListView.as_view(),
        name="post_list",
    ),
    path(
        "posts/create/",
        CreatePostView.as_view(),
        name="create_post",
    ),
]
