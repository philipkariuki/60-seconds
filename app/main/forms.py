from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentsForm(FlaskForm):

    
    comment_section_id = TextAreaField('Insert Comment here')
    submit = SubmitField('Submit')


class PitchesForm(FlaskForm):
    review = TextAreaField('Create Pitch')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')