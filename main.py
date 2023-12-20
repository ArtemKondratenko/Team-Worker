from flask import Flask

from src.database import db, create_tables
from src.request_handler import api


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdb"
app.secret_key = "h3uNFUANxnnxjzgnKAOF399"
app.register_blueprint(api)

db.init_app(app)
create_tables(app)

app.run()
