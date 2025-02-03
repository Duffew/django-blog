from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
# This test does the following
# Firstly, it defines a function, or class method, named test_form_is_valid
# It then creates an instance of our CommentForm and fills out the body field of the form with 
# a string - This is a great post. A dictionary with the field as the key and the content as 
# the value is used. A form with more fields would have a matching number of key:value pairs.
# Finally, it uses an assert to determine if the form is valid. We'll discuss more about assertions below. 
# We've also seen the is_valid() method before too. Since the body field is required, 
# and we have provided some content, the test should pass.
# The test passes. This is indicated by a dot . and the word OK in the terminal.
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'comment'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')


# Some of these methods, such as assertFalse allow us to create negative tests. 
# These are tests that pass when something returns an error.
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid())