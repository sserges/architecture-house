from app import db

class Message(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(255))
    content     = db.Column(db.Text)
    created_at  = db.Column(db.DateTime, default=db.func.now())


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref="post", lazy='dynamic')
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(255))
    author_email       = db.Column(db.String(255))
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
