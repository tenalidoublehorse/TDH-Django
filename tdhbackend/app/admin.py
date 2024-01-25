from django.contrib import admin
from .models import BlogPost,Banner,IndusData,Products
# Register your models here.

import csv
from django.http import HttpResponse

class AdminProducts(admin.ModelAdmin):
    list_display = ('Products_id','Title','Short_desc','Long_desc','Upload_url','Body','Slug','Image1','Image2','Image3','Image4','Image5')



class AdminBlogpost(admin.ModelAdmin):
    list_display=('id','image','title','shortdesc','postdate','authorname')

class AdminBanner(admin.ModelAdmin):
    list_display=('id','SliderId','Title','Image')

class AdminIndusData(admin.ModelAdmin):
    list_display=('id','Firstname','Lastname','Email','Phonenumber','PurposeofContact','Message','AddedTimeStamp')
    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"



admin.site.register(Products,AdminProducts)
admin.site.register(BlogPost,AdminBlogpost)
admin.site.register(Banner,AdminBanner)
admin.site.register(IndusData,AdminIndusData)