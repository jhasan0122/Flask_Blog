from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskBlog.config import Config




db = SQLAlchemy()                                          # database initialization  #
bcrypt = Bcrypt()                                           # encryption initialization #
login_manager = LoginManager()                              # create a login manager object for authorization
login_manager.login_view = 'users.login'                            # for showing Please log in to access this page. for direct account access #
login_manager.login_message_category = 'info'                # bootstrap class add #

mail = Mail()





def create_app(config_class=Config):
    app = Flask(__name__)  # For flask __main__ #
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskBlog.users.routes import users
    from flaskBlog.posts.routes import posts
    from flaskBlog.main.routes import main
    from flaskBlog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

