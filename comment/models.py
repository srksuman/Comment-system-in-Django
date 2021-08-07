from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description =  RichTextField()

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comments = models.TextField()
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True)
