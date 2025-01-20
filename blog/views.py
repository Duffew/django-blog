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

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
