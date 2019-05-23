from application import app, manager, db
from flask_script import Server
from flask_migrate import Migrate, MigrateCommand

import www
# from api.v1 import create_blueprint_v1
# app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

# web server
manager.add_command('runserver', Server(
    host='0.0.0.0',             # 这样在内网才能访问，ubuntu关闭防火墙ufw disable/enable
    port=app.config['SERVER_PORT'],     # 属性通过app获取配置文件
    use_debugger=True,
    use_reloader = True
))

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
# python manage.py db init/migrate/upgrade/downgrade


def main():

    manager.run()


if __name__ == '__main__':
    print(app.config['VERSION'])
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()

