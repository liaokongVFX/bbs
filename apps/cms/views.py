# -*- coding: utf-8 -*-
# Time    : 2019/4/28 22:01
# Author  : LiaoKong

from flask import Blueprint, render_template, request, session, redirect, url_for, views

from .forms import LoginForm
from .models import CMSUser
from .decorators import login_required

import config

bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route("/")
@login_required
def index():
    return render_template("cms/cms_index.html")


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
                session[config.CMS_USER_ID] = user.id
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


@bp.route("/logout/")
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for("cms.login"))


@bp.route("/profile/")
@login_required
def profile():
    return render_template("cms/cms_profile.html")


class ResetpwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template("cms/cms_resetpwd.html")

    def post(self):
        pass


bp.add_url_rule("/resetpwd/", view_func=ResetpwdView.as_view("resetpwd"))
