from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Comments, Pitches, Categories
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
# app = create_app('production')
app = create_app('development')


manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Comments=Comments, Pitches=Pitches, Categories=Categories)


if __name__ == '__main__':
    manager.run()