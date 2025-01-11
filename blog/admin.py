from django.contrib import admin
# import the Post model and register it.
# The dot in front of models indicates that we are importing Post from a file named models, 
# which is in the same directory as our admin.py file. 
# If you have multiple models that you want to import, then you can separate them with a comma. 
# For example, in future topics, you will create a Comment model, which will need to be imported at that point.
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# Below the imports, but above the existing registered models, add a class named PostAdmin
# The decorator (@admin) is how we register a class, compared to just registering the standard model
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

# import the Post model and register it.
# This will allow you to create, update and delete blog posts from the admin panel. 
# However, please refrain from adding any posts at the moment, 
# as there are more fields to be added to the tables in an upcoming topic.

# When we create a custom model and we want it to appear in the admin site, then we need to tell Django 
# by registering it in the admin.py file. That is what admin.site.register does.
# We import our custom Post model above
# Now we have a decorator above the PostAdmin class; delete the existing Post model registration.
# admin.site.register(Post)

# admin.site.register method takes only one argument. If you are registering multiple models, 
# you would need a separate line for each model. 
admin.site.register(Comment)

