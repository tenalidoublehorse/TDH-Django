from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import BlogPost
from .serializers import  BlogPostSerializer


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
# @api_view(['POST'])
# def deleteUser(request,id):
#     if request.method == 'POST':
#         queryset = user.objects.get(UserID=id)
#         queryset.UserStatus = False
#         user_details = {  
#                 'UserID':0,	
#                 'EmailID' :'',	
#                 'Password'  :'',	
#                 'Role':'',	
#                 'UserStatus':'',		
#         }
#         user_details['UserID'] = queryset.UserID
#         user_details['EmailID'] = queryset.EmailID
#         user_details['Password'] = queryset.Password
#         user_details['Role'] = queryset.Role
#         user_details['UserStatus'] = queryset.UserStatus
       
#         serializer_data = UserSerializer(instance=queryset ,data = user_details)
#         if serializer_data.is_valid():
#             serializer_data.save()
#         return Response(serializer_data.data)
     