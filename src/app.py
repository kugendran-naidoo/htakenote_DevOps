# comment
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import inspect
import sys


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class NotesDB(db.Model):

    note_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Note %r>' % self.note_id


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        note_content = request.form['content']
        new_note = NotesDB(content=note_content)

        try:
            db.session.add(new_note)
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Error adding your Note'

    else:
        all_the_notes = NotesDB.query.order_by(NotesDB.date_created).all()
        return render_template('index.html', all_notes=all_the_notes)


@app.route('/delete/<int:note_id>')
def delete(note_id):

    note_to_delete = NotesDB.query.get_or_404(note_id)

    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect('/')

    except Exception:
        return 'Error deleting your Note'


@app.route('/update/<int:note_id>', methods=['GET', 'POST'])
def update(note_id):

    note_to_update = NotesDB.query.get_or_404(note_id)

    if request.method == 'POST':
        note_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Error updating your Note'
    else:
        return render_template('update.html', note=note_to_update)


def divit(numerator, denominator):

    try:
        # current function name
        func_name = inspect.stack()[0][3]

        error_msg = "Only Real numbers are supported."

        if (denominator == 0):
            return None

    except ValueError as e:
        print(func_name + " - " + error_msg)
        print(e)
        raise
        sys.exit(1)

    else:

        return numerator/denominator


if __name__ == "__main__":
    app.run(debug=True)
