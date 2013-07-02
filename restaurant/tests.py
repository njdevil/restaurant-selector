from django.test import TestCase
from django.template.defaultfilters import slugify
from django.db import connection, transaction
from fueled.restaurant.models import Restaurant, Comment
import random

class RestaurantTest(TestCase):
    def testRestaurantSlug(self):
        input="This is the 1st restaurant to be slugged."
        expected="this-is-the-1st-restaurant-to-be-slugged"
        processed=slugify(input)
        self.assertEqual(processed,expected)

    def testCommentCount(self):
        random_id=random.randrange(1,9)
        django_comment_count=len(Comment.objects.filter(restaurant=random_id).values())

        cursor=connection.cursor()
        cursor.execute("select count(0) from restaurant_comment where restaurant_id="+str(random_id))
        sql_comment_count=int(cursor.fetchone()[0])
        self.assertEqual(django_comment_count, sql_comment_count)

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
