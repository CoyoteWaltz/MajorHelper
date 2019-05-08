import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

class Application(Flask):
    # app工厂
    def __init__(self, import_name, template_folder=None):
        super(Application, self).__init__(import_name, template_folder)
        self.config.from_object('config.base_settings')
        if "ops_config" in os.environ:
            self.config.from_object('config.%s_settings' %os.environ["ops_config"])
        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__)
# 支持跨域请求
CORS(app, resource={
    r'{}/*'.format(app.config['VERSION']) : {'origins' : '*'}
})
manager = Manager(app)
