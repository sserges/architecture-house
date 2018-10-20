import flask_admin
from flask import url_for
from flask_admin import helpers as admin_helpers
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib import sqla

from app import app, db
from .models import (
    Role,
    User,
    Post,
    Comment,
    Message
)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class PostView(MyModelView):
    create_template = 'blog/post_create.html'
    edit_template = 'blog/post_edit.html'
    form_widget_args = {
        'content': {
            'id': 'editor'
        }
    }


admin = flask_admin.Admin(
    app,
    "La maison de l'architecte: Administration",
    base_template='my_master.html',
    template_mode='bootstrap3',
)

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(Message, db.session))
admin.add_view(PostView(Post, db.session))
admin.add_view(MyModelView(Comment, db.session))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )
