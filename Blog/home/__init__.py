from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)

#import secrete..secrete.token_hex(25)..the Below value
app.config['SECRET_KEY'] = 'bafea63b59c168017b6a3d27313ec48a30fca4b2c289497808'

#creating sqlite database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
log_manager = LoginManager(app)
log_manager.login_view = 'login'
log_manager.login_message_category ='info'



from home import routes
