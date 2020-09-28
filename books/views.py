from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializer import PostSerializer
# Create your views here.

class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer