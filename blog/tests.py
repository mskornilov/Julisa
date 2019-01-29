from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category
# Create your tests here.

def create_user():
    user = User.objects.create(username='kms', password='lutik1lutik1')
    user.save()
    
def create_post():
    category_id = 1
    user = User.objects.get(id=1)
    post = Post.objects.create(category_id=category_id, author=user, status='published',
                               title="Test post")
    post.save()
    return post

class PostTestCase(TestCase):
    def test_status_200(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

    def test_post_creation(self):
        create_user()
        post = create_post()
        self.assertEqual(post.title, 'Test post')
