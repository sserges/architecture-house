from flask import (
    render_template,
    url_for,
    redirect,
    flash,
    request
)

from app import app, db
from .models import Message, Post
from .forms import MessageForm

@app.route('/')
def home():
    k
    form = MessageForm(request.form)
    return render_template('home.html', form=form)


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        email = str(form.email.data).strip()
        content = str(form.content.data).strip()

        message = Message(email=email, content=content)

        db.session.add(message)
        db.session.commit()

        flash('Votre message a été envoyé avec succès. Nous reviendrons à vous très bientôt.', 'success')
        return redirect(url_for('home'))

    return render_template('home.html', form=form)


@app.route('/blog')
def home_blog():
    posts = Post.query.all()
    return render_template('blog/home_blog.html', posts=posts)
