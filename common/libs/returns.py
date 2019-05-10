from flask import jsonify


def success_return(data):
    # 请求成功
    return jsonify(
        {
            "msg" : "请求成功",
            "data" : data,
            "code" : 2001
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
            "code" : 4
        }
    )
