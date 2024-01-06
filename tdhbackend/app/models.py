from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


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