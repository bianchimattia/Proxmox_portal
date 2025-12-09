from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    admin = User(username='admin', email='admin@example.com', role='admin')
    admin.set_password('password123')
    db.session.add(admin)
    db.session.commit()
    print("Admin creato")
