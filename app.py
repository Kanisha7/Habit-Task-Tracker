from flask import Flask, render_template
from models import db
from routes import app_routes

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "your_secret_key"


db.init_app(app)

# Register routes from routes.py
app.register_blueprint(app_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)
app = Flask(__name__, template_folder="templates")
