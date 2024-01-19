from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import BlogPost,Banner,IndusData
from .serializers import  BlogPostSerializer,BannerSerializer,IndusfoodsSerializer


def index(request):
    return render(request, 'uifiles/index.html')

def the_journey(request):
    return render(request, 'uifiles/thejourney.html')

def where_we_are(request):
    return render(request, 'uifiles/where-we-are.html')

def awards_recognitions(request):
    return render (request, 'uifiles/awards-and-recognitions.html')

def csr_initiatives(request):
    return render(request, 'uifiles/csr-initiatives.html')

def csr_gallery(request):
    return render(request, 'uifiles/csr-gallery.html')

def csr_gallery_two(request):
    return render(request, 'uifiles/csr-gallery-two.html')

def tdh_products(request):
    return render(request, 'uifiles/tdh-products.html')

def product_details(request):
    return render(request, 'uifiles/product-details.html')

def news_room(request):
    return render(request, 'uifiles/news-room.html')

def news_room_two(request):
    return render(request, 'uifiles/news-room-two.html')

def news_room_three(request):
    return render(request, 'uifiles/news-room-three.html')

def contact(request):
    return render(request, 'uifiles/contact.html')



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

@api_view(['GET'])
def getIndusData(request):
    if request.method == 'GET':
        queryset = IndusData.objects.all()
        serializer_data = IndusfoodsSerializer(queryset ,many=True)
        return Response(serializer_data.data)