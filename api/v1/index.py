from common.libs.redprint import Redprint


from application import db, app

api = Redprint('index')


# index页面?干嘛呢？
@api.route('/')
def index():
    
    
    return 'hello world'