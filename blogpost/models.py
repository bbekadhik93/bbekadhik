from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class SEOInformation(models.Model):
    topicname= models.CharField(max_length=64,blank=True)
    title= models.TextField(max_length=100,blank=True)
    url= models.CharField(max_length=64,blank=True)
    seotitle= models.TextField(max_length=100,blank=True)
    seodescription= models.TextField(max_length=1000,blank=True)
    image= models.ImageField(max_length=100,blank=True)
    keyword= models.TextField(max_length=100,blank=True)
    infomessage= models.TextField(max_length=1000,blank=True)
    reasearchtime= models.DateTimeField(default=datetime.now)
    summary= models.TextField(blank=True)
    details= RichTextField(blank=True)
    writtentime= models.DateTimeField(default=datetime.now)
    publish= models.BooleanField(default=False)
    publishedtime= models.DateTimeField(default=datetime.now)

    def __str__(self):
                return self.topicname
