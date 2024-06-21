from flask import render_template, redirect, url_for, flash, request
from app import db
from app.auth import bp
from app.models import User
from app.auth.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Chat, Document
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

model = AutoModelForQuestionAnswering.from_pretrained('./app/model')
tokenizer = AutoTokenizer.from_pretrained('./app/model')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        question = request.form['question']
        # Asumiendo que podrías tener un contexto relevante (podrías ajustar esto)
        context = "" #Contexto que puedas cargar basado en la lógica que definas para RAG
        # Preparar los datos para el modelo
        inputs = tokenizer.encode_plus(question, context, return_tensors="pt", add_special_tokens=True)
        outputs = model(**inputs)
        # Obtener la respuesta del modelo
        answer_ids = torch.argmax(outputs.logits, dim=-1)
        answer = tokenizer.decode(answer_ids[0], skip_special_tokens=True)

        # Guardar en base de datos
        new_chat = Chat(question=question, answer=answer, user_id=current_user.id)
        db.session.add(new_chat)
        db.session.commit()

        # Refrescar la página con la respuesta
        return redirect(url_for('auth.chat'))

    chats = Chat.query.filter_by(user_id=current_user.id).all()
    return render_template('chat.html', chats=chats)