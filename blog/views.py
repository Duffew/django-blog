from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


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
        },     
    )
