from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask

app=Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


class Venue(db.Model):
    __tablename__ = 'venues'

    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String)
    city                = db.Column(db.String(130))
    state               = db.Column(db.String(130))
    address             = db.Column(db.String(130))
    phone               = db.Column(db.String(130))
    image_link          = db.Column(db.String(500))
    facebook_link       = db.Column(db.String(130))
    website_link        = db.Column(db.String(130))
    seeking_talent      = db.Column(db.Boolean, default = False)
    seeking_description = db.Column(db.String(600))
    show                = db.relationship('Show', backref='Venue', lazy=True)


class Artist(db.Model):
    __tablename__ = 'artists'

    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String)
    city                = db.Column(db.String(130))
    state               = db.Column(db.String(130))
    phone               = db.Column(db.String(130))
    genres              = db.Column(db.String(130))
    facebook_link       = db.Column(db.String(130))
    image_link          = db.Column(db.String(500))
    website_link        = db.Column(db.String(130))
    seeking_venue       = db.Column(db.Boolean, default = False)
    seeking_description = db.Column(db.String(600))
    show                = db.relationship('Show', backref='Artist', lazy=True)


class Show(db.Model):
    __tablename__= 'shows'

    id          = db.Column(db.Integer, primary_key=True)
    venu        = db.Column(db.Integer, db.ForeignKey(Venue.id))
    artist      = db.Column(db.Integer, db.ForeignKey(Artist.id))
    start_time  = db.Column(db.DateTime)

