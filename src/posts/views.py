from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer


class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Post.objects
            .filter(is_deleted=False)
            .select_related("author", "original_post")
            .prefetch_related("media")
        )
