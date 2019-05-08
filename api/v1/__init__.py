from flask import Blueprint
from api.v1 import index, locate, general, detail

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    index.api.register(bp_v1)
    locate.api.register(bp_v1)
    general.api.register(bp_v1)
    detail.api.register(bp_v1)

    return bp_v1


