from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm


# Create your views here.
# create a class-based view named PostList that inherits from the generic.ListView class to display all your posts.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # replace the existing template_name with the new template_name 
    # and add a paginate_by into the PostList class-based view.
    # You can now delete the redundant post_list.html template, as we've replaced it with the new index.html template.
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # added in POST lessons
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        # Inside the if statement, we create an instance of the CommentForm class 
        # using the form data that was sent in the POST request. In our case, the form data is the comment's text. 
        # As specified in forms.py, this will be stored in the body field.
        # We then assign this instance to a variable named comment_form.
        comment_form = CommentForm(data=request.POST)
        # Firstly, we check to see if the form is valid.
        if comment_form.is_valid():
            # Then, we call the comment_form's save method with commit=False. Calling the save method 
            # with commit=False returns an object that hasn't yet been saved to the database so that we can 
            # modify it further. We do this because we need to populate the post and author fields before we save. 
            # The object will not be written to the database until we call the save method again.
            comment = comment_form.save(commit=False)
            # We can then modify the object by setting the author field of the comment to the current request.user - the user 
            # who is currently logged in. We also set the post field using the post variable, which contains 
            # the result of the get_object_or_404 helper function at the start of the view code.
            comment.author = request.user
            comment.post = post
            # Now, we can finally call the save method to write the data to the database.
            comment.save()
            messages.add_message(request, messages.SUCCESS,'Comment submitted and awaiting approval'
    )
    # Outside the if statement, we create a blank instance of the CommentForm class. This line resets the content of the form to 
    # blank so that a user can write a second comment if they wish.
    comment_form = CommentForm()

    print("About to render template")

    return render(
        request,
        "blog/post_detail.html",
        # below is a python dictionary
        # We retrieved one single blog post, stored it in a variable called post and passed that through 
        # to the template in a dictionary where both the value and key name was, you guessed it, post. 
        # This is called context and it is how you pass data from your own views to a template.
        {"post": post,
        # added is POST lessons
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },     
    )
