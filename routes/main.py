from flask import Blueprint, render_template, request, redirect, session
from models import UserModel, TaskModel

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    username = session.get("username")
    if not username:
        return redirect("/login")

    user_id = UserModel.get_id(username)
    if not user_id:
        session.clear()
        return redirect("/login")

    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            TaskModel.add(task, user_id)

    tasks = TaskModel.get_all_by_user(user_id)
    return render_template("index.html", tasks=tasks, username=username)

@main_bp.route("/delete", methods=["POST"])
def delete():
    username = session.get("username")
    if not username:
        return redirect("/login")
    
    user_id = UserModel.get_id(username)
    task_id = request.form.get("id")
    if user_id and task_id:
        TaskModel.delete(task_id, user_id)
    return redirect("/")

@main_bp.route("/toggle", methods=["POST"])
def toggle():
    username = session.get("username")
    if not username:
        return redirect("/login")
    
    user_id = UserModel.get_id(username)
    task_id = request.form.get("id")
    if user_id and task_id:
        TaskModel.toggle(task_id, user_id)
    return redirect("/")

@main_bp.route("/edit", methods=["POST"])
def edit():
    username = session.get("username")
    if not username:
        return redirect("/login")
    
    user_id = UserModel.get_id(username)
    task_id = request.form.get("id")
    new_content = request.form.get("new_content", "").strip()
    if user_id and task_id and new_content:
        TaskModel.update(task_id, new_content, user_id)
    return redirect("/")
