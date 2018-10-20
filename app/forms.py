from wtforms import (
    Form,
    StringField,
    TextAreaField
)

from wtforms.validators import (
    Email,
    DataRequired
)

class MessageForm(Form):
    email = StringField('Email', [DataRequired(), Email()])
    content = TextAreaField('Message', [DataRequired()])


class CommentForm(Form):
    name = StringField('Nom', [DataRequired()])
    content = TextAreaField('Commentaire', [DataRequired()])
    # email = StringField('Email', [Email()])
    
