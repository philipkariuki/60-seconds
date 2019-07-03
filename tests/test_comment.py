import unittest
from app.models import Comments, User
from flask_login import current_user
from app import db

class TestComments(unittest.TestCase):

    def setUp(self):
        self.user_Phil = User(username = 'Phil',password = 'potato', email = 'phli@ymail.com')
        self.new_comments = Comments(id=1, comment_section_id='This is a commentary',pitches_id = 2,user_id= 1 )

    def tearDown(self):
        Comments.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comments,Comments))


    