from django.urls import path

from .views import CreatePostView, PostListView, UpdatePostView. RetrievePostView, UploadMediaView, CreateCommentView, CommentListView, RetrieveCommentView

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
    path(
        "posts/<uuid:pk>/update/",
        UpdatePostView.as_view(),
        name="update_post",
    ),
    path(
        "posts/<uuid:pk>/",
        RetrievePostView.as_view(),
        name="retrieve_post",
    ),
    path(
        "posts/<uuid:pk>/delete/",
        DeletePostView.as_view(),
        name="delete_post",
    ),
    path(
        "posts/media/",
        UploadMediaView.as_view(),
        name="upload_media",
    ),
    path(
        "posts/<uuid:post_id>/comments/",
        CommentListView.as_view(),
        name="post_comments",
    ),
    path(
        "comments/",
        CreateCommentView.as_view(),
        name="create_comment",
    ),
    path(
        "comments/<uuid:pk>/",
        RetrieveCommentView.as_view(),
        name="retrieve_comment",
    ),
]
