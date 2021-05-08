from flask import Flask

app = Flask(__name__)

from webapp.main.routes import main
from webapp.statistics.routes import statistics
from webapp.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(statistics)
app.register_blueprint(errors)