

from clubsapp import create_app

app = create_app()

from clubsapp import db

with app.app_context():
  db.drop_all()
  db.create_all()
