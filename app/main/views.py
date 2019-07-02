
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import CommentsForm,UpdateProfile,PitchesForm
from ..models import Categories,User, Pitches,Comments
from flask_login import login_required, current_user
from .. import db,photos
import markdown2




@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    categories = Categories.get_categories()
    title = 'Pitch please'
    return render_template('index.html', title = title, categories = categories )












@main.route('/categories/<int:id>')
def categories(id):
    '''
    category route function returns a list of pitches chosen and allows users to create a new pitch
    '''

    categories = Categories.query.get(id)

    if categories is None:
        abort(404)
        
    pitches = Pitches.get_pitches(id)
    title = "Pitches"
    return render_template('categories.html', title = title, categories = categories,pitches = pitches)

# Dynamic routing for pitches
@main.route('/categories/pitches/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitches(id):
    '''
    Function to check Pitches form
    '''
    form = PitchesForm()
    categories = Categories.query.filter_by(id=id).first()

    if categories is None:
        abort(404)

    if form.validate_on_submit():
        review = form.review.data
        # user = current_user._get_current_object()
        new_pitches = Pitches(review=review,user_id=current_user.id,category_id=categories.id)
        new_pitches.save_pitches()
        return redirect(url_for('.categories', id = categories.id))

    title = 'New pitch'
    return render_template('newpitches.html', title = title, pitches_form = form)

# Dynamic routing for one pitch
@main.route('/pitches/<int:id>', methods = ['GET','POST'])
@login_required
def single_pitch(id):
    
    pitches = Pitches.query.get(id)

    if pitches is None:
        abort(404)

    comments = Comments.get_comments(id)
    title = 'Comment Section'
    return render_template('pitch.html', title = title, pitches = pitches, comments = comments )


# Dynamic routing for comment section
@main.route('/pitches/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentsForm()
    pitches = Pitches.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment_section_id = form.comment_section_id.data
        new_comment = Comments(comment_section_id=comment_section_id, user_id=current_user.id,pitches_id=pitches.id)
        new_comment.save_comments()
        return redirect(url_for('.categories', id = pitches.id))

    title = 'New Comment'
    return render_template('comments.html', title = title, comment_form = form)






@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)





@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



