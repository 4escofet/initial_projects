from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db, model, tokenizer
from app.main import bp
from app.models import User, Chat
import torch
import os

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        question = request.form['question']
        print(f"Received question: {question}")
        print(f"Using model type: {os.environ.get('MODEL_TYPE')}")
        print(f"Model: {model}")
        print(f"Tokenizer: {tokenizer}")

        if os.environ.get('MODEL_TYPE') == 'qa':
            inputs = tokenizer.encode_plus(question, add_special_tokens=True, return_tensors="pt")
            input_ids = inputs["input_ids"].tolist()[0]

            answer_start_scores, answer_end_scores = model(**inputs)
            answer_start = torch.argmax(answer_start_scores)
            answer_end = torch.argmax(answer_end_scores) + 1
            
            answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
        else:
            inputs = tokenizer.encode(question, return_tensors="pt")
            outputs = model.generate(inputs, max_length=50, do_sample=True, top_k=10, top_p=0.95, num_return_sequences=1)
            answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        new_chat = Chat(question=question, answer=answer, user_id=current_user.id)
        db.session.add(new_chat)
        db.session.commit()

        return redirect(url_for('main.chat'))
    
    chats = Chat.query.filter_by(user_id=current_user.id).all()
    return render_template('chat.html', chats=chats)
