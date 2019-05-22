from common.libs.redprint import Redprint

from flask import request
# from application import db, app

# from common.models.models import 

api = Redprint('index')


# index页面?干嘛呢？
@api.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        d_args = request.args
        d_get_json = request.get_json()
        d_values = request.values.get('content')
        d_data = request.data
        d_json = request.json
        d_form = request.form

        print('args')
        print(d_args)

        print('get json')
        print(d_get_json)

        print(d_json)

        print('values')
        print(type(d_values))
        for i in eval(d_values):
            print(i)

        print('data')
        print(d_data)

        print('form')
        print(d_form)


    
        return 'hello world'

    if request.method == 'POST':
        # d_values = request.values.get('content')
        d_values = request.get_json()

        print(d_values)
        print(request.headers)
        return 'post'






# 马克思注意学院文=>马克思学院 id=1, 24
# 社会科学学部=>括号都不要         id=2, 21
