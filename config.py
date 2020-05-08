from os import path
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('/etc/copilot/app.cfg')
