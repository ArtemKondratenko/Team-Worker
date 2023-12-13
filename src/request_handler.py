from flask import Blueprint, redirect, render_template, request
from src import db, auth

api = Blueprint("api", __name__)


@api.get("/pages/create_user")
def get_register_user_page():
    return render_template("create_user.html")


@api.post("/create_user")
def register_user():
    username = request.form["username"]
    password = request.form["password"]
    try:
        db.add_user(
            name=username,
            password=password,
        )
        return "Пользователь успешно зарегистрирован"
    except Exception as e:
        raise f"Ошибка при регистрации: {str(e)}"


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
