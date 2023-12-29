from django.contrib import admin
from .models import BlogPost,Banner
# Register your models here.
class AdminBlogpost(admin.ModelAdmin):
    list_display=('id','image','title','shortdesc','postdate','authorname')

class AdminBanner(admin.ModelAdmin):
    list_display=('id','Title','Image')

admin.site.register(BlogPost,AdminBlogpost)
admin.site.register(Banner,AdminBanner)