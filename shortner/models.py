from flask_sqlalchemy import SQLAlchemy
from example import app

db = SQLAlchemy()


class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(10), index=True, Unique = True)
    url = db.Column(db.String(255))
    url_title = db.Column(db.String(511))
 
    def __init__(self, short_url, url, url_title):
        self.short_url = short_url
        self.url = url
        self.url_title = url_title
