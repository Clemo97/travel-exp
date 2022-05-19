import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User
from flask_script import Manager ,Server
# Creating app instance



app = create_app('development')

app.config['appSECRET_KEY'] ='123456789'

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('Tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()