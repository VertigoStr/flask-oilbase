# flask-oilbase

flask-oilbase is a simple site that was made on flask with MongoDB.

# Install
- Install [MongoDB](https://www.mongodb.org/downloads#production)
- Install [Python](https://www.python.org/downloads/)
- Create virtual enviroment:
    - python -m venv myvenv
- Install Flask and packages:
    - run virtual enviroment
    - pip install flask
    - pip install flask-script
    - pip install WTForms
    - pip install mongoengine
    - pip install flask_mongoengine
    - Install [Flask-Admin](https://github.com/flask-admin/Flask-Admin/tree/master/examples/forms)
    - Install [Flask-Navigation](https://github.com/tonyseek/flask-navigation):
        - pip install Flask-Navigation
        
# Run
- Run mongodb as daemon:
    - mongod --dbpath "DB PATH" --storageEngine=mmapv1
- Run server:
    - python manage.py runserver
