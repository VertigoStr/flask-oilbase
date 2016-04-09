from datetime import datetime
from flask import url_for
from oilsite import db
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView


class Descriptions(db.Document):
	__tablename__ = "Описания"
	title = db.StringField(max_length=255, required=True)
	description = db.StringField(required=True)
	image = db.ListField(db.StringField(max_length=100))

class Slogans(db.Document):
	__tablename__ = "Слоганы"
	title = db.StringField(max_length=255, required=True)
	description = db.StringField(required=True)
	page = db.StringField(max_length=20, required=True)

class Dilers(db.Document):
	__tablename__ = "Дилеры"
	city = db.StringField(max_length=100, required=True)
	address = db.StringField(max_length=400, required=True)
	phone = db.StringField(max_length=30, required=True)
	coords = db.StringField(max_length=30, required=True)
	email = db.StringField(required=True)

class Personal(db.EmbeddedDocument):
	__tablename__ = "Персонал"
	name = db.StringField(max_length=250, required=True)
	post = db.StringField(max_length=250, required=True)
	phone = db.StringField(max_length=30, required=True)
	email = db.StringField(required=True)

class Departaments(db.Document):
	__tablename__ = "Отделы"
	title = db.StringField(max_length=100, required=True)
	worktime = db.ListField(db.StringField(max_length=100))
	personal = db.ListField(db.EmbeddedDocumentField('Personal'))

	def __unicode__(self):
		return self.title

	meta = {
		'allow_inheritance':True
	}

class Contacts(db.Document):
	__tablename__ = "Контакты"
	name = db.StringField(max_length=450, required=True)
	address = db.StringField(max_length=250, required=True)
	coords = db.StringField(max_length=30, required=True)
	site = db.StringField(max_length=20, required=True)
	email = db.StringField(required=True)

class CallBack(db.Document):
	__tablename__ = "Обратная связь"
	name = db.StringField(max_length=200, required=True)
	email = db.StringField(max_length=20, required=True)
	phone = db.StringField(max_length=20, required=True)
	message = db.StringField(required=True)

class Products(db.EmbeddedDocument):
	__tablename__ = "Товары"
	title = db.StringField(max_length=100, required=True)
	image = db.StringField(max_length=100, required=True)
	description = db.StringField(max_length=250, required=True)
	content = db.StringField(max_length=100, required=True)
	gost = db.StringField(max_length=250, required=True)
	docs = db.StringField(max_length=250, required=True)
	cost = db.IntField(required=True)
	send_type = db.StringField(max_length=250, required=True)


class Categories(db.Document):
	__tablename__ = "Категории"
	title = db.StringField(max_length=100, required=True)
	description = db.StringField(required=True)
	products = db.ListField(db.EmbeddedDocumentField('Products'))
