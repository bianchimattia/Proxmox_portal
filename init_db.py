from app import create_app, db

from app.models.user import User
from app.models.vm import VMRequest  

app = create_app()

with app.app_context():
    db.create_all()
    print("tabelle create")
