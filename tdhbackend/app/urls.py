from django.urls import path
from .views import getBlogpost, getBpost
urlpatterns = [
   path('blog/', getBlogpost, name="blog"),
   path('blogsingle/<int:id>', getBpost, name="blogsingle")
]