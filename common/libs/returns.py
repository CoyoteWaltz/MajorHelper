from flask import jsonify


def success_return(data):
    # 请求成功
    return jsonify(
        {
            "msg" : "请求成功",
            "data" : data,
            "code" : 2000
        }
    )

def request_disallow_return(method):
    # 请求方式错误
    return jsonify(
        {
            "msg" : "{method} allowed".format(method=method),
            "code" : 4005,
        }
    )

def failed_return(msg):
    # 内部错误，
    return jsonify(
        {
            "msg" : msg,
            "data" : None,
            "code" : 4001
        }
    )

def db_failed_return():
    # 数据库操作错误
    return jsonify(
        {
            "msg" : "数据库操作错误",
            "code" : 4000
        }
    )

def db_not_found():
    # 数据库操作错误
    return jsonify(
        {
            "msg" : "数据库中未找到",
            "code" : 4004
        }
    )
