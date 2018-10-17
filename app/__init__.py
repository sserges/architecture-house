from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
# from app.models import Post, Message

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name='microblog', template_mode='bootstrap3')


from app import routes, models, errors

admin.add_view(ModelView(models.Message, db.session))
admin.add_view(ModelView(models.Post, db.session))