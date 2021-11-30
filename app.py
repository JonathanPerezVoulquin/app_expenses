from flask import Flask, request, url_for, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECREY_KEY'] = 'asddasasd'

db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.Integer)
    expense = db.Column(db.Integer)
db.create_all()

@app.route('/')
def home():
    trans = Transaction.query.all()
    return render_template('index.html', trans = trans)


@app.route('/transaction-create', methods=['POST'])
def get_transaction():
    tran = Transaction(entry= request.form['entryCash'], expense = request.form['expenses'])
    db.session.add(tran)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)