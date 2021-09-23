import datetime as dt

from .models import db

if __name__ == "__main__":
    print("Initializing database and creating data models...")
    db.create_all()
    db.session.commit()
    print("Done.")
