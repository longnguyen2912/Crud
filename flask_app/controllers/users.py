from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect("/user")


@app.route('/user')
def users():
    return render_template("read.html", users=User.get_all())


@app.route('/user/new')
def to_add_page():
    return render_template("create.html")


@app.route('/user/create', methods=['POST'])
def add_user():
    print(request.form)
    User.save(request.form)
    return redirect("/user")


@app.route('/user/showone/<int:id>')
def show_one(id):
    data = {
        "id":id
    }
    return render_template("display_user.html", user=User.show_one(data))


@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        "id":id
    }
    return render_template("update.html", user=User.show_one(data))


@app.route('/user/update', methods=['POST'])
def user_update():
    User.update(request.form)
    return redirect("/user")


@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect("/user")


@app.route('/user/delete', methods=['POST'])
def delete():
    User.delete(request.form)
    return redirect("/user")
