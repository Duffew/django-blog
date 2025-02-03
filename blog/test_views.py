from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):

    # The setUp method is a special method we can use in our tests to provide initial settings for our tests to use.
    def setUp(self):
        # In this case, we create a superuser and a small blog post in our test database. This data is then assigned 
        # as a variable of the self object. (You'll learn more about self in a moment).
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        # To run our post_detail view, we need an instance of Post to render. As an instance of Post requires a ForeignKey 
        # to a User for its author field, we first needed to create a superuser to author the blog post: author=self.user.
        # You can then define all the fields your database instance(s) requires for the tests by using the imported model, 
        # in this case, the Post model, and providing values for its relevant fields.
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        # In the test method, we use reverse to generate a URL for accessing the post_detail view, 
        # providing 'blog-title' as an argument.
        # This 'blog-title' is the slug for the blog post, which we previously created 
        # as self.post during the setUp method.
        # Then, we use self.client.get() with this URL to send a GET request to the post_detail view.
        # The response from the view is then captured in the response variable.
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        # confirms that the view responds successfully, a fundamental check for any web page.
        self.assertEqual(response.status_code, 200)
        # ensure that the content we defined for self.post in setUp (the blog title and content) will be rendered 
        # as part of the response, verifying that our view correctly displays the blog post.
        # You might have noticed the use of a different type of string literal in our test code: b"". This syntax 
        # is for creating byte strings, which is crucial because all internet data, including the HTTP response 
        # content in response.content, is in byte format. This differs from Python's standard use of Unicode strings.
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        # checks that the correct form is being used in the context.
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        # Commenting on a blog post is reserved for authenticated users, so a user must log in before commenting. 
        # We use the username and password previously defined in the setUp method to test this step.
        self.client.login(
            username="myUsername", password="myPassword")
        # post_data is a dictionary of fields, which uses the 'body' form field as the key and a string of text as the comment value. 
        # This dictionary contains the data posted to the database.
        post_data = {
            'body': 'This is a test comment.'
        }
        # In the POST response, you use the post() method with the reverse method as an argument, plus an additional argument 
        # of the post_data dictionary to post data to the database. This second argument is the comment the user is posting.
        response = self.client.post(reverse(
            'post_detail', args=['blog-title']), post_data)
        # The first assertion confirms that the HTTP response code is 200, which indicates that the reverse succeeded. 
        # The second assertion confirms the string 'Comment submitted and awaiting approval' is included in the response.
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )
        # The test failed with a 404 status code instead of 200, as the 'blog' argument in args didn't match the 
        # 'blog-title' slug of our mock blog post created in the setUp method. 
        # Correcting args to ['blog-title'] aligns with the defined slug, resolves the issue 
        # and returns a successful 200 status code, indicating the page is found.