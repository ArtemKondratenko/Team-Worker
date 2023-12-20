from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase, MappedAsDataclass):
    pass


db = SQLAlchemy(model_class=Base)


def create_tables(app):
    with app.app_context():
        # db.drop_all()
        db.create_all()
