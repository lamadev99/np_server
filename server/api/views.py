from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from api.models import *
from api.serializers import *
from api.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .pagination import MyPagination
from rest_framework.decorators import action


# Create your views here.

class WriterProfileViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    queryset = Writer.objects.all()
    serializer_class = WriterPorfileSerializer
    if queryset.count() > 0:
        pagination_class = MyPagination

class NewsViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    queryset = News.objects.all().order_by('-updated_at')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'subCategory', 'keywords', 'is_writer_pick', 'is_featured']
    search_fields = ['^category', '^subCategory', '^title', '^keywords']
    if queryset.count() > 0:
        pagination_class = MyPagination

    @action(detail=True, methods=['get'])
    def mostPopular(self, request, pk=None):
        popular = News.objects.all().order_by('-updated_at', '-views')[:5]
        popular_serializer = NewsSerializer(popular,many=True, context={'request':request })
        return Response(popular_serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    queryset = Comment.objects.all().order_by('-cId')
    serializer_class = CommentSerializer
    if queryset.count() > 0:
        pagination_class = MyPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class PageGeneratorViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    queryset = PageGenerator.objects.all()
    serializer_class = PageGeneratorSerializer