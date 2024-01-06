from django.contrib import admin
from .models import BlogPost,Banner,IndusData
# Register your models here.
class AdminBlogpost(admin.ModelAdmin):
    list_display=('id','image','title','shortdesc','postdate','authorname')

class AdminBanner(admin.ModelAdmin):
    list_display=('id','SliderId','Title','Image')

class AdminIndusData(admin.ModelAdmin):
    list_display=('id','Firstname','Lastname','Email','Phonenumber','PurposeofContact','Message','AddedTimeStamp')

admin.site.register(BlogPost,AdminBlogpost)
admin.site.register(Banner,AdminBanner)
admin.site.register(IndusData,AdminIndusData)