from django.contrib import admin
from .models import BlogPost
# Register your models here.
class AdminBlogpost(admin.ModelAdmin):
    list_display=('id','image','title','shortdesc','postdate','authorname')


admin.site.register(BlogPost,AdminBlogpost)