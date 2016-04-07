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

class Personal(db.EmbeddedDocument):
	name = db.StringField(max_length=250, required=True)
	post = db.StringField(max_length=250, required=True)
	phone = db.StringField(max_length=30, required=True)
	email = db.StringField(required=True)

class Departaments(db.Document):
	title = db.StringField(max_length=100, required=True)
	worktime = db.ListField(db.StringField(max_length=100))
	personal = db.ListField(db.EmbeddedDocumentField('Personal'))

	def __unicode__(self):
		return self.title

	meta = {
		'allow_inheritance':True
	}

class Contacts(db.Document):
	name = db.StringField(max_length=450, required=True)
	address = db.StringField(max_length=250, required=True)
	coords = db.StringField(max_length=30, required=True)
	site = db.StringField(max_length=20, required=True)
	email = db.StringField(required=True)

class CallBack(db.Document):
	name = db.StringField(max_length=200, required=True)
	email = db.StringField(max_length=20, required=True)
	phone = db.StringField(max_length=20, required=True)
	message = db.StringField(required=True)

class Products(db.EmbeddedDocument):
	title = db.StringField(max_length=100, required=True)
	image = db.StringField(max_length=100, required=True)
	description = db.StringField(max_length=250, required=True)
	content = db.StringField(max_length=100, required=True)
	gost = db.StringField(max_length=250, required=True)
	docs = db.StringField(max_length=250, required=True)
	cost = db.IntField(required=True)
	send_type = db.StringField(max_length=250, required=True)


class Categories(db.Document):
	title = db.StringField(max_length=100, required=True)
	description = db.StringField(required=True)
	products = db.ListField(db.EmbeddedDocumentField('Products'))

