from django.db import models
# Add a new import at the top for the User model.
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# As you can see, this uses a constant STATUS. Create this constant above the class as a tuple.
# A draft is defined as zero and published as one, so you can see the default is to save as a draft.
STATUS = ((0, "Draft"), (1, "Published"))
# Create a class named Post inheriting from the Model class.
class Post(models.Model):
    """

    Stores a single blog post entry related to :model:`auth.User`
    
    In a Django model class, you will also need to include any models its 
    ForeignKeys are related to, hence :model:`auth.User`.
    Note: that we’ve prefaced the model with the label model: and enclosed the model name 
    with markdown backticks in the docstrings to state unambiguously that the word User 
    in the docstring refers to the model User in the auth app.

    """
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
    # We've integrated a new field named featured_image, using the imported CloudinaryField class. 
    # This class allows users to upload media to a database model
    # If "placeholder" is there, then the default.jpg file in our static folder should be displayed. 
    # Otherwise, the user-generated image stored on Cloudinary is shown.
    featured_image = CloudinaryField('image', default='placeholder')
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


    # Let's start by adding a class Meta to our Post model. 
    # Note: You should add this at the bottom of the Post Model under the fields.
    class Meta:
        ordering = ["-created_on"]
    
    # Now, add a method to our Post model. Note: Methods should always be below Meta classes.
    def __str__(self):
        return f"The title of the post is {self.title} | written by {self.author}"


# Underneath the Post model, create a new Comment model. Python convention dictates that we 
# leave two blank lines between the end of one class and the start of a new one.
# Using the completed ERD and what you have learned from creating the Post model, add the correct fields.
# All of the fields should have lower-case names and underscores in place of spaces.
class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`
    """
    post = models.ForeignKey(
        # While the Post model above doesn't have a field named comments, the related_name in our Comment model sets up a logical link, 
        # effectively creating this association. This is what is called a reverse lookup. 
        # We don't access the Comment model directly.
        # Instead, we fetch the related data from the perspective of the Post model.
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    # Add metadata to the Comment model that orders the comments with the oldest first.
    class Meta:
        ordering = ["created_on"]
    
    # Add a Python str dunder method to the Comment model 
    # that returns a string in the format shown in the topic image.
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
