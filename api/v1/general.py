
from werkzeug.exceptions import HTTPException  # 这里面各种异常定义了
from common.libs.redprint import Redprint
from common.libs.returns import *


api = Redprint('general')

@api.route('/')
def general():
    data = {
        'majors' : [
            {
                'name' : 'xx',
                'college' : 'ligong',
                'rank' : 20.3
            },
            {
                'name' : 'yy',
                'college' : 'renwen',
                'rank' : 20.3
            },
            {
                'name' : 'zz',
                'college' : 'jingguan',
                'rank' : 40.3
            },
            {
                'name' : 'pp',
                'college' : 'ligong',
                'rank' : 22.1
            }
        ]
    }
    # print(data)  
    return success_return(data)