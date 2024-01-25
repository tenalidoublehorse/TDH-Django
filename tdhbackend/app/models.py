from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

ProductType = [
      ('Consumer_pack','Consumer_pack'),
      ('Commercial_pack','Commercial_pack')
]


class Products(models.Model):
    Products_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Product_type = models.CharField(max_length=200,choices=ProductType,null=True,default="")
    Short_desc = models.CharField(max_length=200)
    Long_desc = models.CharField(max_length=1000)
    Upload_url = models.URLField(default="")
    Body = RichTextField(max_length=1000)
    Slug = models.CharField(max_length=200,unique=True,null=True)
    Image1 = models.ImageField(upload_to='uploads/')
    Image2 = models.ImageField(upload_to='uploads/')
    Image3 = models.ImageField(upload_to='uploads/')
    Image4 = models.ImageField(upload_to='uploads/')
    Image5 = models.ImageField(upload_to='uploads/')
    Related_products = models.CharField(max_length=200,default="",null=True)


    def __str__(self):
          return self.Title
    


class Contact(models.Model):
      Firstname = models.CharField(max_length=100)
      Lastname = models.CharField(max_length=100)
      Email = models.CharField(max_length=50)
      Phonenumber = models.CharField(max_length=10)
      Purpose = models.CharField(max_length=100)
      Subject = models.CharField(max_length=500)
      Message = models.CharField(max_length=1000)

      def __str__(self):
            return self.Firstname

    



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=225,default="uradgota")
    image = models.ImageField(upload_to='uploads/')
    masonryimage = models.ImageField(upload_to='uploads/')
    fullview = models.CharField(max_length=225,default="col-lg-3")
    title = models.CharField(max_length=225)
    shortdesc = models.CharField(max_length=225)
    postdate = models.CharField(max_length=225)
    authorname = models.CharField(max_length=50)
    longdescription = RichTextField(blank=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
            return self.title

class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    SliderId = models.IntegerField(default=0)
    Title = models.CharField(max_length=225)
    Image = models.ImageField(upload_to='uploads/')
    def __str__(self):
            return self.Title
    

class IndusData(models.Model):
    id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField()
    Phonenumber = models.CharField(max_length=50)
    PurposeofContact = models.CharField(max_length=50,blank=True,null=True)
    Message = models.CharField(max_length=500 ,blank=True,null=True)
    AddedTimeStamp	 = models.DateTimeField(default=timezone.now)
    updatedTimeStamp	= models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.Firstname