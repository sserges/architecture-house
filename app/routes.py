from flask import (
    render_template,
    url_for,
    redirect,
    flash,
    request
)

from app import app, db
from .models import Message, Post, Comment
from .forms import MessageForm, CommentForm


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


@app.route('/blog/posts/<int:id>', methods=['GET', 'POST'])
def post_detail(id):
    post = Post.query.filter_by(id=id).first_or_404()
    form = CommentForm(request.form)
    if request.method == 'POST':
        if form.validate():
            name = str(form.name.data).strip()
            content = str(form.content.data).strip()
            new_comment = Comment(
                author_name=name,
                content=content,
                post_id=post.id
            )

            db.session.add(new_comment)
            db.session.commit()

            return redirect(url_for('post_detail', id=post.id))

    context = {
        'post': post,
        'form': form,
    }

    return render_template('blog/post_detail.html', **context)
