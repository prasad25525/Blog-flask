from flask_wtf import FlaskForm  
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,TextAreaField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from home.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators =[DataRequired(),
                            Length(min=5,max=15)])
    email = StringField('Email',validators=[DataRequired([])])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username was already taken.')

    def validate_email (self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That Email was already taken.')
    

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=5, max=15)])
    email = StringField('Email', validators=[DataRequired([])])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That Username was already taken.')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('That Email was already taken.')


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    submit = SubmitField('Post')
