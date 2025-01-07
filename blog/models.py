from django.db import models
# Add a new import at the top for the User model.
from django.contrib.auth.models import User

# Create your models here.

# As you can see, this uses a constant STATUS. Create this constant above the class as a tuple.
# A draft is defined as zero and published as one, so you can see the default is to save as a draft.
STATUS = ((0, "Draft"), (1, "Published"))
# Create a class named Post inheriting from the Model class.
class Post(models.Model):
    # In the Post model, add an attribute title defined as a character field with a max length of 200 characters.
    title = models.CharField(max_length=200, unique=True)
    # In the Post model, add an attribute slug defined as a slug field with a max length of 200 characters.
    # In publishing, a slug is a short name for an article that is still in production. 
    # It comes from the lead casts used in print typesetting. 
    # You can tell Django was created for the newspaper industry! 
    # In Django, the slug is what you'll use to build a URL for each of your posts. 
    # You'll learn more about this in an upcoming lesson.
    slug = models.SlugField(max_length=200, unique=True)
    # In the Post model, add an attribute author defined as a Foreign Key to the User model.
    # One user can write many posts, so this is a one-to-many or Foreign Key. 
    # The cascade on delete means that on the deletion of the user entry, all their posts are also deleted.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # In the Post model, add an attribute content defined as a text field.
    # This is the blog article content.
    content = models.TextField()
    # In the Post model, add an attribute created_on defined as a date time field.
    # The auto_now_add=True means the default created time is the time of post entry.
    created_on = models.DateTimeField(auto_now_add=True)
    # In the Post model, add an attribute status defined as an integer field with a default of 0.
    # As you can see, this uses a constant STATUS. Create this constant above the class as a tuple.
    status = models.IntegerField(choices=STATUS, default=0)
    # In the Post model, add a new field named excerpt using the TextField field type. As the excerpt is optional, 
    # the user must be able to leave this database row blank without throwing an error.
    excerpt = models.TextField(blank=True)
    # Using what you have learned, add a field called updated_on to the Post model.
    # The field is the same type as created_on but should have the argument of auto_now=True instead.
    updated_on = models.DateTimeField(auto_now=True)


# Underneath the Post model, create a new Comment model. Python convention dictates that we 
# leave two blank lines between the end of one class and the start of a new one.
# Using the completed ERD and what you have learned from creating the Post model, add the correct fields.
# All of the fields should have lower-case names and underscores in place of spaces.
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
