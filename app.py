from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.String(20), default=datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    def __repr__(self):
        return f"Todo('{self.task}', '{self.completed}', '{self.timestamp}')"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        return redirect('/')
    else:
        todos = Todo.query.order_by(Todo.timestamp.desc()).all()
        return render_template('index.html', todos=todos)


@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=815)
