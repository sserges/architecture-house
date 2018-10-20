from flask_security import UserMixin, RoleMixin

from app import db

class Message(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(255))
    content     = db.Column(db.Text)
    created_at  = db.Column(db.DateTime, default=db.func.now())


class Post(db.Model):
    __tablename__ = 'posts'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(255))
    content     = db.Column(db.Text)
    comments    = db.relationship('Comment', backref="post", lazy='dynamic')
    created_at  = db.Column(db.DateTime, default=db.func.now())
    updated_at  = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Comment(db.Model):
    __tablename__ = 'comments'

    id              = db.Column(db.Integer, primary_key=True)
    author_name     = db.Column(db.String(255))
    author_email    = db.Column(db.String(255))
    content         = db.Column(db.Text)
    post_id         = db.Column(db.Integer, db.ForeignKey('posts.id'))


# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id          = db.Column(db.Integer(), primary_key=True)
    name        = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id              = db.Column(db.Integer, primary_key=True)
    first_name      = db.Column(db.String(255))
    last_name       = db.Column(db.String(255))
    email           = db.Column(db.String(255), unique=True)
    password        = db.Column(db.String(255))
    active          = db.Column(db.Boolean())
    confirmed_at    = db.Column(db.DateTime())
    roles           = db.relationship('Role', secondary=roles_users, 
                        backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email