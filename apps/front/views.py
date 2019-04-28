# -*- coding: utf-8 -*-
# Time    : 2019/4/28 22:02
# Author  : LiaoKong


from flask import Blueprint

bp = Blueprint("front", __name__)


@bp.route("/")
def index():
    return "front index"
