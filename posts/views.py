from rest_framework import generics,permissions
from posts.models import Post
from posts.serializers import PostSerializer,PostTestSerializer
from django.views.decorators.csrf import csrf_exempt


class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostTestSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer


class PostTestList(generics.ListAPIView):
    model = Post
    serializer_class = PostTestSerializer
    permission_classes = [
        permissions.AllowAny
    ]



