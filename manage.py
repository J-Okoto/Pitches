from app import create_app,db
from flask_script import Manager,Server
from app.models import Pitch,PitchCategory,User,Role,Comment

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Pitch= Pitch,Pitchcategory=PitchCategory, Role = Role, Comment = Comment,User=User )

manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()