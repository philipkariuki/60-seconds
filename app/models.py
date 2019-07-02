from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comments',backref = 'user',lazy = "dynamic")
    pitches = db.relationship("Pitches", backref="user", lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Pitches(db.Model):

    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitches_id = db.Column(db.Integer)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    date_posted = db.Column(db.DateTime,default=datetime.now)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    comment = db.relationship("Comments", backref="peptalk", lazy = "dynamic")
    review = db.Column(db.String)
    



    def save_pitches(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_pitches(cls,id):

        response =cls.query.order_by(Pitches.date_posted.desc()).filter_by(category_id=id).all()
        return response




class Categories(db.Model):
    __tablename__ = 'categories'

    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    
    def save_categories(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Categories.query.all()
        return categories




class Comments(db.Model):
    '''
    Comment class that creates new comments from users in pitches
    '''
    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer,primary_key = True)
    comment_section_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comments(self):
        '''
        Save the comments per pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(pitches_id=id).all()
        return comment

