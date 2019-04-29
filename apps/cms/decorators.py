# -*- coding: utf-8 -*-
# Time    : 2019/4/29 9:40
# Author  : LiaoKong

from functools import wraps

from flask import session, redirect, url_for

import config


def login_required(fuc):
    @wraps(fuc)
    def inner(*args, **kwargs):
        if config.CMS_USER_ID in session:
            return fuc(*args, **kwargs)
        else:
            return redirect(url_for("cms.login"))

    return inner
