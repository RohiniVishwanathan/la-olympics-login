LA Olympics 2028 – Login & Signup Integration
This branch contains the login and signup functionality built with Flask and integrated with SQLite3.

 Features

Styled login.html and signup.html pages in /templates
Integrated with database.db using SQLAlchemy
Users table stores username and password
Flash messages enabled for invalid login or signup success
Signup redirect back to login on success
 Files Added / Modified

app.py → Contains login/signup Flask routes and database logic
templates/login.html → Updated with a sign-up link and new layout
templates/signup.html → New sign-up page
database.db → SQLite3 database with users table
init_db.py → Used to initialize the database (can be removed after setup)
 How to Run

Make sure you’re in a virtual environment
Run:
python3 app.py
Go to:
http://127.0.0.1:5000/login

Notes- 

Existing login page by Tracie is currently named login.html. If merging, consider renaming or replacing to avoid conflict.
Once integrated with the main app, update login redirect targets accordingly.
