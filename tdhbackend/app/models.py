from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

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