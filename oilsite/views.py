from flask.ext.mongoengine.wtf import model_form
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from oilsite.models import *

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


oilsite.add_url_rule('/', view_func=MainPage.as_view('main'))
oilsite.add_url_rule('/delivery', view_func=DeliveryPage.as_view('delivery'))
oilsite.add_url_rule('/dilers', view_func=DilersPage.as_view('dilers'))