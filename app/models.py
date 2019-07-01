from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

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
    piches_id = db.Column(db.Integer)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    review = db.Column(db.String)
    



    def save_pitches(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_pitches(cls,id):

        response =cls.query.filter_by(pitches_id = id).all()
        return response















