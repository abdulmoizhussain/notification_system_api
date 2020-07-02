# -*- coding: utf-8 -*-
from flask_script import Manager as _Manager
from flask_migrate import Migrate as _Migrate, MigrateCommand as _MigrateCommand
from application import app as _app, db as _db

migrate = _Migrate(_app, _db)
manager = _Manager(_app)
manager.add_command('db', _MigrateCommand)

if __name__ == '__main__':
    manager.run()
