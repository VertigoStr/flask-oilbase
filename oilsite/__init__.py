from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "mng_oilbase"}
app.config["SECRET_KEY"] = "password"

db = MongoEngine(app)

def register_blueprints(app):
	from oilsite.views import oilsite
	app.register_blueprint(oilsite)

register_blueprints(app)

if __name__ == '__main__':
    app.run()