# -*- coding: utf-8 -*-
# Time    : 2019/4/28 22:02
# Author  : LiaoKong

from flask import Blueprint

bp = Blueprint("common", __name__, url_prefix="/common")


@bp.route("/")
def index():
    return "common index"
