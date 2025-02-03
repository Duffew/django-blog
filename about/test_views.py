
from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm

# Create a new test case with an appropriate name, and ensure it inherits from the TestCase class.
class TestAboutViews(TestCase):
    
    # Set up a mock instance of the About model so that your about view can use it.
    # The setUp method initialises conditions needed before each test runs.
    def setUp(self):
        self.about_content = About(title="About Me", content="This is about me!")
        self.about_content.save()

    # Create a test method with an appropriate name.
    def test_the_about_page(self):
        # Assert that.
        response = self.client.get(reverse('about'))
        # The about page loads successfully.
        self.assertEqual(response.status_code, 200)
        # The about page contains text from the mock About instance.
        self.assertIn(b'About Me', response.content)
        # The collaborate_form context for this view is an instance of CollaborateForm.
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
        'name': 'test name',
        'email': 'test@email.com',
        'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)


    