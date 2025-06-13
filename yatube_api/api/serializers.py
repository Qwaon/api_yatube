from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        source='author.username',
        read_only=True
    )

    class Meta:
        exclude = ()
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
    )

    class Meta:
        exclude = ()
        model = Comment
        read_only_fields = ('post',)
