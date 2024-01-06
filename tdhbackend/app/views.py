from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import BlogPost,Banner
from .serializers import  BlogPostSerializer,BannerSerializer,IndusfoodsSerializer


@api_view(['GET'])
def getBlogpost(request):
    if request.method == 'GET':
        queryset = BlogPost.objects.all()
        serializer_data = BlogPostSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    
@api_view(['GET'])
def getBpost(request,id):
    if request.method == 'GET':
        queryset = BlogPost.objects.get(id=id)
        serializer_data = BlogPostSerializer(queryset ,many=False)
        return Response(serializer_data.data)   

@api_view(['GET'])
def getBanner(request):
    if request.method == 'GET':
        queryset = Banner.objects.order_by("SliderId")
        serializer_data = BannerSerializer(queryset ,many=True)
        return Response(serializer_data.data)
    

@api_view(['POST'])
def addIndusData(request):
    if request.method == 'POST':
        indus_data = IndusfoodsSerializer(data = request.data)
        if indus_data.is_valid():
            indus_data.save()
            return Response(indus_data.initial_data, status=status.HTTP_201_CREATED)
        return Response(indus_data.errors, status=status.HTTP_400_BAD_REQUEST)
     