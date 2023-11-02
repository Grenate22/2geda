from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from . models import Post
from . serializers import PostSerializers



class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend,SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title','description','location']

   
    
    def perform_create(self, serializer):
          serializer.save(user=self.request.user)
