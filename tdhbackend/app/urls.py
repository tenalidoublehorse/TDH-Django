from django.urls import path
from .views import index, the_journey, where_we_are, awards_recognitions, csr_initiatives,csr_gallery,csr_gallery_two,tdh_products,product_details,news_room,news_room_two,news_room_three,contact,getBlogpost,getBpost,getBanner,addIndusData,getIndusData,DownloadBroacher


urlpatterns = [
   path('',index, name="index"),
   path('the-journey/', the_journey, name="the_journey"),
   path('where-we-are/', where_we_are, name="where_we_are"),
   path('awards-recognitions/', awards_recognitions, name="awards_recognitions"),
   path('csr-initiatives/', csr_initiatives, name="csr_initiatives"),
   path('csr-gallery/', csr_gallery, name="csr_gallery"),
   path('csr-gallery-two/', csr_gallery_two, name="csr_gallery_two"),
   path('tdh-products/', tdh_products, name="tdh_products"),
   path('product-details/<str:slug>', product_details, name="product_details"),
   # path('product-details-two/', product_details_two, name="product_details_two"),
   path('news-room/', news_room, name="news_room"),
   path('news-room-two/', news_room_two, name="news_room_two"),
   path('news-room-three/', news_room_three, name="news_room_three"),
   path('contact/', contact, name="contact"),
   path('blog/', getBlogpost, name="blog"),
   path('blogsingle/<int:id>', getBpost, name="blogsingle"),
   path('getbanner/', getBanner , name='getbanner'),
   path('addindusdata/', addIndusData , name='addindusdata'),
   path('getindusdata/', getIndusData , name='getindusdata'),
   path('downloadBroacher/', DownloadBroacher , name='downloadBroacher')
]
