import os
class Config:
    SECRET_KEY = "abdelfatah_secret_key"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads" )
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ="smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "ma0332897@gmail.com"
    MAIL_PASSWPRD= "oldvqthfmdozeasi"
    MAIL_DEFAULT_SENDER= "ma0332897@gmail.com"
