from app2 import app, db
from app2.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User':user, 'Post':post}