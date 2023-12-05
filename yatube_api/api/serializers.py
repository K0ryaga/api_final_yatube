from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import Post, Group, Comment, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'group')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate(self, attrs):
        following_user = attrs.get('following')
        user = self.context['request'].user

        if user == following_user:
            raise serializers.ValidationError(
                "Вы не можете подписаться на себя.")

        if Follow.objects.filter(user=user, following=following_user).exists():
            raise serializers.ValidationError("Вы уже подписаны.")

        return attrs

    class Meta:
        model = Follow
        fields = ('user', 'following')
