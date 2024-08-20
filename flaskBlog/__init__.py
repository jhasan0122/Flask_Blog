from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)                               # For flask __main__ #
app.config['SECRET_KEY'] = '066bb57df532020449df021398de2628'   # For generate a sample secret key and save it #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'    # For database uri  #
db = SQLAlchemy(app)                                          # database initialization  #
bcrypt = Bcrypt(app)                                           # encryption initialization #
login_manager = LoginManager(app)                              # create a login manager object for authorization
login_manager.login_view = 'login'                            # for showing Please log in to access this page. for direct account access #
login_manager.login_message_category = 'info'                # bootstrap class add #


from flaskBlog import routes                              # import rest of the route element #
