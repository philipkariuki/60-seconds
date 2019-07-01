import unittest
from app.models import Comments, User
from flask_login import current_user
from app import db

class TestComments(unittest.TestCase):

    def setUp(self):
        self.user_Phil = User(username = 'Phil',password = 'potato', email = 'phli@ymail.com')
        self.new_comments = Comments(id=1,body='This is a commentary',pitch_id = 2,user_id= 1 )

    def tearDown(self):
        Comments.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comments,Comments))


    
    def test_save_comments(self):
        self.new_comments.save_comments()
        self.assertTrue(len(Comments.query.all())>0)


    def test_get_comments_by_id(self):

        self.new_comments.save_comments()
        got_comments = Comments.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)