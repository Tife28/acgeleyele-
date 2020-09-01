from django.contrib import admin

# Register your models here.
from .models import Post, Sermon
admin.site.register(Post)
admin.site.register(Sermon)