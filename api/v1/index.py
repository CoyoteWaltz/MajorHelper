from common.libs.redprint import Redprint


from application import db, app

api = Redprint('index')

@api.route('/')
def index():
    from sqlalchemy import text
    sql = text('select * from class')
    res = db.engine.execute(sql)
    for row in res:
        app.logger.info(row)
    return 'hello world'