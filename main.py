from flask import Flask

from src.db import create_db
from src.request_handler import api


app = Flask(__name__)
app.secret_key = "h3uNFUANxnnxjzgnKAOF399"

create_db()
app.register_blueprint(api)

app.run()
