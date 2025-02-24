from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Habit, Task

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/")
def index():
    """Render the homepage with all habits and tasks."""
    habits = Habit.query.all()
    tasks = Task.query.all()
    return render_template("index.html", habits=habits, tasks=tasks)

@app_routes.route("/add_habit", methods=["GET", "POST"])
def add_habit():
    """Handle form submission for adding a new habit."""
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        if not name or not description:
            flash("Habit name and description are required!", "error")
            return redirect(url_for("app_routes.add_habit"))

        new_habit = Habit(name=name, description=description)
        db.session.add(new_habit)
        db.session.commit()
        flash("Habit added successfully!", "success")
        return redirect(url_for("app_routes.index"))

    return render_template("add_entry.html")

@app_routes.route("/add_task", methods=["POST"])
def add_task():
    """Handle form submission for adding a new task."""
    title = request.form.get("title")

    if not title:
        flash("Task title is required!", "error")
        return redirect(url_for("app_routes.index"))

    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    flash("Task added successfully!", "success")
    return redirect(url_for("app_routes.index"))

@app_routes.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    """Mark a task as completed."""
    task = Task.query.get(task_id)
    if task:
        task.status = "completed"
        db.session.commit()
        flash(f"Task '{task.title}' marked as completed!", "success")
    else:
        flash("Task not found!", "error")

    return redirect(url_for("app_routes.index"))
