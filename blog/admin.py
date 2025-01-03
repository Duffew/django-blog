from django.contrib import admin
# import the Post model and register it.
from .models import Post

# Register your models here.

# import the Post model and register it.
# This will allow you to create, update and delete blog posts from the admin panel. 
# However, please refrain from adding any posts at the moment, 
# as there are more fields to be added to the tables in an upcoming topic.
admin.site.register(Post)
