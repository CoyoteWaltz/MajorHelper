from application import app
from api.v1 import create_blueprint_v1

"""
在此注册蓝图
"""

app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')