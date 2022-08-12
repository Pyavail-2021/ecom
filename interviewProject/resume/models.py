
from django.db import models
from django.utils.html import format_html
#from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    #content=HTMLField()
    added_date=models.DateTimeField(auto_now_add=True,null=True)
    url=models.CharField(max_length=200)
    image=models.ImageField(upload_to='category/')

    def __str__(Self):
        return Self.title


    def image_tag(self):
        return format_html('<img src= "/media/{}"/>'.format(self.image))


class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content=models.TextField()
    #content=HTMLField()
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    url=models.CharField(max_length=200)
    image=models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title


    def image_tag(self):
        return format_html('<img src= "/media/{}"style="width:70px;height="70px;"/>'.format(self.image))
        
