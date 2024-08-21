import os
class Config:
    SECRET_KEY = '066bb57df532020449df021398de2628'  # For generate a sample secret key and save it #
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # For database uri  #
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')