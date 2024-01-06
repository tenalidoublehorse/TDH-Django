from django.urls import path
from .views import getBlogpost, getBpost,getBanner,addIndusData
urlpatterns = [
   path('blog/', getBlogpost, name="blog"),
   path('blogsingle/<int:id>', getBpost, name="blogsingle"),
   path('getbanner/', getBanner , name='getbanner'),
   path('addindusdata/', addIndusData , name='addindusdata')
]