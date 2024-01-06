from rest_framework import serializers
from .models import BlogPost,Banner,IndusData


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class IndusfoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndusData
        fields = '__all__'