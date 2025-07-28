from django.contrib import admin

from blogapp.models import Blog, Comment, User

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Comment)
