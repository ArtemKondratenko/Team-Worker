from flask import Blueprint, redirect, render_template, request
from src import repository
from src import auth
from src.models import Workspace, Participant

api = Blueprint("api", __name__)


@api.get("/pages/create_user")
def get_register_user_page():
    return render_template("create_user.html")


@api.post("/create_user")
def register_user():
    username = request.form["username"]
    password = request.form["password"]
    try:
        repository.add_user(
            name=username,
            password=password,
        )
        return "Пользователь успешно зарегистрирован"
    except Exception:
        return "Ошибка при регистрации"


@api.get("/pages/login")
def get_login_page():
    return render_template("login.html")


@api.post("/auth")
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = auth.get_user_with_password_check(username, password)
    if not user:
        return "Введён неверный логин или пароль"

    auth.login(user)
    return "Успешная авторизация"


@api.get("/pages/create-workspace")
def get_create_workspace_page():
    return render_template("create-workspace.html")


@api.post("/workspaces")
def create_workspace():
    user = auth.get_current_user_or_raise()

    workspace_name = request.form.get("workspace_name")
    workspace_description = request.form.get("workspace_description")
    workspace = Workspace(name=workspace_name, description=workspace_description)
    repository.save_workspace_in_db(workspace)

    participant = Participant(
        username=user.name, workspace_id=workspace.id, role="leader"
    )
    repository.save_participant_in_db(participant)

    return redirect(f"/workspaces/{workspace.id}")


@api.get("/workspaces/<int:workspace_id>")
def get_workspace(workspace_id: int):
    workspace = repository.get_workspace(workspace_id=workspace_id)
    return render_template("workspace.html", workspace=workspace)
