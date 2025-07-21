from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class Users(AbstractUser):
    pass

class blogs(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=60)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    content=models.CharField(max_length=2000)
    author_id= models.ForeignKey(Users,on_delete=models.CASCADE,editable=False)