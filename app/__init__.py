from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from config import Config

sentry_sdk.init(
    dsn="https://2082154564484487b9776c31a11a125b@sentry.io/1303605",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)




from app import routes, models, admin, errors
