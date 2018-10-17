from app import app, db
from app.models import Message, User, Role
from app.utils import cls

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Message': Message, 'cls': cls, 'User': User, 'Role': Role}
