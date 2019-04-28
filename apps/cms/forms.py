# -*- coding: utf-8 -*-
# Time    : 2019/4/28 22:01
# Author  : LiaoKong

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
    email = StringField(validators=[Email(message="请输入正确格式的邮箱"), InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    remember = IntegerField()
