from app import db
from app import app

# make sure this runs inside the Flask app context
with app.app_context():
    db.create_all()
    print(" Database initialized successfully.")

