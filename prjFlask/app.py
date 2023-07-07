import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models.User import db
from form import NameForm

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app,db)

# rota index
@app.route('/')
def index():
    return render_template('index.html')

# página dinâmica que recupera dados da URL
@app.route('/user')
@app.route('/user/<name>')
def user(name=None):
    print(name)
    return render_template('index.html', name=name)

# cadastro de usuários
@app.route('/user/create', methods=['GET', 'POST'])
def create():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "

    return render_template('create.html', name=name, form=form)