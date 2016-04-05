from datetime import datetime
from flask import url_for
from oilsite import db

class Descriptions(db.Document):
	title = db.StringField(max_length=255, required=True)
	description = db.StringField(required=True)
	image = db.ListField(db.StringField(max_length=100))

class Slogans(db.Document):
	title = db.StringField(max_length=255, required=True)
	description = db.StringField(required=True)
	page = db.StringField(max_length=20, required=True)

class Dilers(db.Document):
	city = db.StringField(max_length=100, required=True)
	address = db.StringField(max_length=400, required=True)
	phone = db.StringField(max_length=30, required=True)
	coords = db.StringField(max_length=30, required=True)
	email = db.StringField(required=True)
