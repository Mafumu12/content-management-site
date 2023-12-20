from django.db import models
import uuid
from django.utils import timezone
from USER_PROFILE.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here. 



 

class categories(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.name)



class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'post_images/')
    body = RichTextField()
    post_id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique = True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    tag = models.ForeignKey(categories,on_delete=models.CASCADE,blank=True,null=True)
    likes = models.ManyToManyField(User, related_name='blog_post',blank=True,null = True )
    
    def total_likes(self):
       return self.likes.count()
    
    def __str__(self):
     return  str(self.title)

    

    
    
    

    
class Comment(models.Model):
   post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
   name = models.CharField(max_length=30)
   body = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
      return '%s - %s' % (self.post.title, self.name)