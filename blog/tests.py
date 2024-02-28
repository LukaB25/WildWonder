from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('tester', password='00000')
        Post.objects.create(
            author=user,
            location_name='Test post',
            slug='test-post',
            location_description='this is the test post',
            hero_image='placeholder.jpg',
            main_content_title='test main content title',
            main_content='test main content',
            latitude='0.0',
            longitude='0.0',
            secondary_content='test secondary content',
            view_count=0,
            comment_count=0,
            approved=True,
            status=0,
            post_code_type=False
            )
        
    def test_location_name_label(self):
        post = Post.objects.get(id=1).location_name
        self.assertEqual(post, 'Test post')

