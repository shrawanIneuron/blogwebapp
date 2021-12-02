import os
class Config:
  SECRET_KEY = '7afdce94c9f759a3e73888b6a578dbda'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
  # SECRET_KEY = os.environ.get('SECRET_KEY')
  # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'shrawankmr95@gmail.com'
  # os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = 'Ucet9142@'