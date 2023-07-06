import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# caminho para a pasta de templates
template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)

# chave para validação de formulários
app.config['SECRET_KEY'] = 'PASSARINHODABARRIGAMARELA'

class NameForm(FlaskForm):
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')

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