from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    #  id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    # default id and password from AbstractUser

    def __str__(self):
        return self.username


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id=models.PositiveIntegerField(primary_key=True, blank=True)
    user = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, to_field="id", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} : {self.content}"
