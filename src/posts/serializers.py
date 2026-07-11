from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "content",
            "original_post",
            "likes_count",
            "comments_count",
            "reposts_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "author",
            "likes_count",
            "comments_count",
            "reposts_count",
            "created_at",
            "updated_at",
        )
