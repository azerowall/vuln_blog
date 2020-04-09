#
#!env/bin/python3

from app import app

@app.shell_context_processor
def make_shell_context():
    from app import db
    from app.models import User
    return {'db': db, 'User': User}

#app.run(debug=True)