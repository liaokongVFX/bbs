# -*- coding: utf-8 -*-
# Time    : 2019/4/28 22:01
# Author  : LiaoKong

from flask import Blueprint, render_template, request, session, redirect, url_for

from .forms import LoginForm
from .models import CMSUser

bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route("/")
def index():
    return "cms index"


@bp.route("/login/", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            password = form.password.data
            email = form.email.data
            remember = form.remember.data

            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session["user_id"] = user.id
                if remember:
                    # 如果设置session.permanent=True 过期时间为31天
                    session.permanent = True

                return redirect(url_for("cms.index"))
            else:
                message = "邮箱或者密码错误"

        else:
            print(list(form.errors.values())[0][0])
            message = list(form.errors.values())[0][0]

    return render_template("cms/cms_login.html", message=message)
