from flask import Flask, render_template
# db import
from datetime import datetime
from flask.ext.mongoengine import MongoEngine

# admin import
from flask_admin.contrib.mongoengine import ModelView
import flask_admin as admin
from flask_admin.form import rules

# navigation import
from flask.ext.navigation import Navigation


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "mng_oilbase"}
app.config["SECRET_KEY"] = "password"

# db part 

db = MongoEngine()
db.init_app(app)

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


# admin part

class DescriptionsView(ModelView):
	column_filters = ['title']
	column_searchable_list = ('title', 'description', )

class SlogansView(ModelView):
	column_filters = ['title']
	column_searchable_list = ('title', 'description', 'page',)

class ContactsView(ModelView):
	column_filters = ['name']
	column_searchable_list = ('name', 'address', 'coords', 'site', 'email',)

class DilersView(ModelView):
    column_filters = ['city']
    column_searchable_list = ('city', 'address', 'phone', 'coords', 'email',)

class CallBackView(ModelView):
	column_filters = ['name']
	column_searchable_list = ('name', 'email', 'phone', 'message', )

class CategoriesView(ModelView):
	column_filters = ['title']
	column_searchable_list = ('title', 'description',)
	form_subdocuments = {
        'products': {
            'form_rules': ('title', rules.HTML('<hr>'), 'code')
        }
    }

class DepartamentsView(ModelView):
	column_filters = ['title']
	column_searchable_list = ('title', )
	form_subdocuments = {
        'personal': {
            'form_rules': ('name', rules.HTML('<hr>'), 'code')
        }
    }

admin = admin.Admin(app, 'Нефтебаза: администрирование')
admin.add_view(DilersView(Dilers))
admin.add_view(CallBackView(CallBack))
admin.add_view(CategoriesView(Categories))
admin.add_view(DepartamentsView(Departaments))
admin.add_view(ContactsView(Contacts))
admin.add_view(DescriptionsView(Descriptions))
admin.add_view(SlogansView(Slogans))

# register blueprints for views

def register_blueprints(app):
	from oilsite.views import oilsite
	app.register_blueprint(oilsite)

register_blueprints(app)

# navigation part
nav = Navigation()
nav.init_app(app)

products_array = []
categs = Categories.objects.all().order_by('title')
for el in categs:
	products_array.append(nav.Item(el.title, 'products', {'product': el.title}))

nav.Bar('top', [
		nav.Item('Продукция','products', {'product':'Бензин'}, items = products_array),
		nav.Item('Доставка', 'delivery'),
		nav.Item('Дилеры', 'dilers'),
		nav.Item('Контакты', 'contacts')
	])


@app.route('/contacts')
def contacts():
	return render_template('oilsite/contacts.html')

@app.route('/dilers')
def dilers():
	return render_template('oilsite/dilers.html')

@app.route('/delivery')
def delivery():
	return render_template('oilsite/delivery.html')

@app.route('/products/<product>/')
def products():
	return render_template('oilsite/products.html', product=product)

# end


if __name__ == '__main__':
	app.run()

