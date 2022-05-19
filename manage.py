<<<<<<< HEAD
from app import create_app
=======
import os
import click
from flask_migrate import Migrate
from app import create_app,db
from app.models import User
>>>>>>> 37784d7e5f883dcbda6d831b929a4f6d3ce1a660
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