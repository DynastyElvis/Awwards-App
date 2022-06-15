from django.test import TestCase

from .models import *

# Create your tests here.

class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create( username='caleb')
        self.post = Post.objects.create( title='post', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, link='http://ur.coml')
        self.rating = Rating.objects.create( design=6, usability=7, content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)