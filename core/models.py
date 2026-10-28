from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid

# Create your models here.
User= get_user_model()

class Profile(models.Model):
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    id_user= models.IntegerField()
    bio= models.TextField(blank=True)
    profile_img= models.ImageField(upload_to="profile_images", default= 'blank_profile_picture.jpg')
    location= models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='post_images')
    content= models.TextField()
    posted_at= models.DateTimeField(default=datetime.now)
    like_count= models.IntegerField(default=0)