# Habit-Task-Tracker

## Overview
The **Habit & Task Tracker** is a simple web-based application built using **Flask** and **SQLAlchemy**. It helps users track their daily habits and tasks, allowing them to mark them as completed.

## Features
- Add, view, and complete **habits**.
- Add, view, and complete **tasks**.
- Flash messages for notifications.
- SQLite database for persistent data storage.
- Minimal and clean UI with **HTML, CSS, Flask**.

## Technologies Used
- **Python** (Flask, SQLAlchemy)
- **HTML & CSS**
- **SQLite**

## Installation & Setup

### Prerequisites
Ensure you have **Python 3** installed on your system.

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/Habit-Task-Tracker.git
   cd Habit-Task-Tracker
   ```

2. **Create a virtual environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```sh
   flask db init  # Run only if using Flask-Migrate (first-time setup)
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
   If not using Flask-Migrate, manually create the database:
   ```python
   from app import db
   db.create_all()
   ```

5. **Run the Flask application**
   ```sh
   flask run
   ```

6. **Open in your browser**
   Go to `http://127.0.0.1:5000/`.

## Usage
- **Add a Habit:** Click "Add Habit" and enter the habit details.
- **Complete a Habit:** Click "Mark as Completed" next to a habit.
- **Add a Task:** Enter a task in the form and submit.
- **Complete a Task:** Click "Mark as Completed" next to a task.

## Project Structure
```
Habit-Task-Tracker/
│── app.py              # Flask app entry point
│── models.py           # Database models
│── routes.py           # Flask routes
│── templates/          # HTML templates
│   ├── index.html      # Home page
│   ├── add_entry.html  # Add Habit page
│── static/
│   ├── styles.css      # Styling for the app
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

## Contributing
Feel free to submit pull requests or open issues to improve the project.

## License
This project is licensed under the **MIT License**.

---
🚀 Happy Tracking!

