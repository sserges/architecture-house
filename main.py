from app import app
from app.models import Message
from app.utils import cls

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Message': Message, 'cls': cls}
