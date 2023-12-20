from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    name =  models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField()
    profession = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='img',blank=True,null=True,default='images/default.png')
    about = models.TextField()
    profile_id = models.UUIDField(default=uuid.uuid4, editable = False, unique=True, primary_key=True)

    def __str__(self):
        return str(self.username)
