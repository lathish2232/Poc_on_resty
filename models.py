import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from . import settings
from . import app

app.config.update(settings.database)
db = SQLAlchemy(app)


class MobiUsers(db.Model):
    __tablename__ = "mobi_users"

    user_id = db.Column(db.Text, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)

class NamedSearch(db.Model):
    __tablename__ = "named_search"

    id = db.Column(db.Integer, primary_key=True)
    accont_id =db.Column(db.Text, db.ForeignKey(MobiUsers.user_id), nullable=False)
    name = db.Column(db.Text, nullable=False)
    criteria = db.Column(db.Text, nullable=False)
    last_executed = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=True)
    created_date = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=True)

