from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError


from posts.models import Post, Group, Follow
from .serializers import (PostSerializer,
                          GroupSerializer,
                          CommentSerializer,
                          FollowSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    authentication_classes = [JWTAuthentication]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    authentication_classes = [JWTAuthentication]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self._get_post(self.kwargs['post_id']).comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self._get_post(self.kwargs['post_id']))

    def _get_post(self, post_id):
        return get_object_or_404(Post, id=post_id)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        search_param = self.request.query_params.get('search', None)
        if search_param:
            queryset = queryset.filter(
                following__username__icontains=search_param)
        return queryset

    def perform_create(self, serializer):
        following_user = serializer.validated_data['following']
        user = self.request.user

        if user == following_user:
            raise ValidationError("Вы не можете подписаться на себя.")

        if Follow.objects.filter(user=user, following=following_user).exists():
            raise ValidationError("Вы уже подписаны.")

        serializer.save(user=user)
