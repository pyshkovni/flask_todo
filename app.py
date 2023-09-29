## Задачи
# 1. Разобраться с механизмом работы элементов flask-приложения
# -> 2. Написать приложение-заметчик, в котором можно добавлять заметки, удалять их и менять статус заметки (выпонено/невыполнено)
# 3. Запустить приложение на сервере.
# https://flask.palletsprojects.com/en/2.3.x/quickstart/

# импорт класса веб-приложения и базы данных
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# создание экземпляра приложения с базой данных
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Хранение информации о заметках в модели Todo
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)


@app.route("/", methods=["GET"])
def index():
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form["content"]
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<todo_id>", methods=["GET"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<todo_id>", methods=["GET"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


# Запуск файла
if __name__ == '__main__':
    # оператор with работает с контекстным менеджером. 
    # позволяет закрыть соединение с БД после выхода из оператора with 
    with app.app_context():
        db.create_all()
    app.run()  # host='0.0.0.0'
    
