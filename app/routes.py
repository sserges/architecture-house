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


@app.route('/', methods=['GET', 'POST'])
def home():
    form = MessageForm(request.form)
    if request.method == 'POST':
        if form.validate():
            email = str(form.email.data).strip()
            content = str(form.content.data).strip()

            message = Message(email=email, content=content)

            db.session.add(message)
            db.session.commit()

            flash('Votre message a été envoyé avec succès. Nous reviendrons à vous très bientôt.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Erreur ! Veuillez vérifier les données saisies.', 'danger')

    return render_template('home.html', form=form)


@app.route('/blog/posts/')
def home_blog():
    posts = Post.query.all()
    return render_template('blog/post_list.html', posts=posts)


@app.route('/blog/posts/<int:id>')
def post_detail(id):
    post = Post.query.filter_by(id=id).first_or_404()
    return render_template('blog/post_detail.html', post=post)
