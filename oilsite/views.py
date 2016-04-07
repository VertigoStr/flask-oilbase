from flask.ext.mongoengine.wtf import model_form
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from oilsite.models import *
from wtforms import *

oilsite = Blueprint('oilsite', __name__, template_folder='templates')

class MainPage(MethodView):

	def get_context(self):
		desc = Descriptions.objects(image__size=1)
		carousel = Slogans.objects(page=u'Главная')

		context = {
			"desc":desc,
			"carousel":carousel
		}

		return context

	def get(self):
		context = self.get_context()
		return render_template('oilsite/main.html', **context)


class DeliveryPage(MethodView):

	def get_context(self):
		desc = Descriptions.objects(image__size=3)
		carousel = Slogans.objects(page=u'Доставка')

		context = {
			"desc":desc,
			"carousel":carousel
		}
		
		return context

	def get(self):
		context = self.get_context()
		return render_template('oilsite/delivery.html', **context)


class DilersPage(MethodView):

	def get(self):
		dilers = Dilers.objects.all()
		return render_template('oilsite/dilers.html', dilers=dilers)

class ContactsPage(MethodView):

	form = model_form(CallBack, field_args = {
		'name' : {'description':"Ваше имя"},
		'email' : {'description':"Ваш почтовый адрес"},
		'phone' : {'description':"Ваш телефон"},
		'message' : {'description':"Ваше сообщение"},
		})

	def get_context(self):
		contacts = Contacts.objects.all()
		departs = Departaments.objects.all()
		departaments = Departaments.objects(title = u"Администрация").get()
		main_persons = departaments['personal']
		departaments = Departaments.objects(title = u"Центр поставок").get()
		send_persons = departaments['personal']
		form = self.form(request.form)

		context = {
			"form":form,
			"contacts":contacts,
			"departs":departs,
			"main_persons":main_persons,
			"send_persons":send_persons
		}

		return context

	def get(self):
		context = self.get_context()
		return render_template('oilsite/contacts.html', **context)

	def post(self):
		context = self.get_context()
		form = context.get('form')

		if form.validate():
			callback = CallBack()
			form.populate_obj(callback)
			callback.save()

			return redirect(url_for('oilsite.contacts'))

		return render_template('oilsite/contacts.html', **context)


class ProductsPage(MethodView):

	def get_context(self, product):
		flag = False
		product = product.strip()
		categories = Categories.objects.all()

		prev_el = Categories.objects(title__lt=product)
		if prev_el.first() is None:
			prev_el = Categories.objects().all()[len(Categories.objects) - 1].title
		else:
			prev_el = prev_el[len(prev_el) - 1].title

		next_el = Categories.objects(title__gt=product).first()
		if next_el is None:
			next_el = Categories.objects().first().title
		else:
			next_el = next_el.title

		item = {"current": product, "next":next_el, "prev":prev_el}
		product = Categories.objects(title=product).get()['products']
		context = {
			"categories":categories,
			"product":product,
			"item":item
		}

		return context

	def get(self, product):
		context = self.get_context(product)
		return render_template('oilsite/products.html', **context)


oilsite.add_url_rule('/', view_func=MainPage.as_view('main'))
oilsite.add_url_rule('/dilers', view_func=DilersPage.as_view('dilers'))
oilsite.add_url_rule('/delivery', view_func=DeliveryPage.as_view('delivery'))
oilsite.add_url_rule('/contacts', view_func=ContactsPage.as_view('contacts'))
oilsite.add_url_rule('/products/<product>/', view_func=ProductsPage.as_view('products'))