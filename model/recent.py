import datetime as dt
from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class MobiUsers(db.Model):
    __tablename__ = "mobi_users"

    user_id = db.Column(db.Text, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)

class NamedSearch(db.Model):
    __tablename__ = "named_search"

    id = db.Column(db.BigInteger, primary_key=True)
    accont_id =db.Column(db.Text, db.ForeignKey(MobiUsers.user_id), nullable=False)
    name = db.Column(db.Text, nullable=False)
    criteria = db.Column(db.Text, nullable=False)
    Last_executed = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=False)
    created_date = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=False)

class RecentSearch(db.Model):
    __tablename__ = "recent_search"
    
    id = db.Column(db.BigInteger, primary_key=True)
    accont_id =db.Column(db.Text, db.ForeignKey(MobiUsers.user_id), nullable=False)
    criteria = db.Column(db.Text, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    Last_executed = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=False)
    created_date = db.Column(db.DateTime, default=dt.datetime.utcnow, nullable=False)

