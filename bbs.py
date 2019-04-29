# -*- coding: utf-8 -*-
# Time    : 2019/4/28 21:57
# Author  : LiaoKong

from flask import Flask
from flask_wtf import CSRFProtect

from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp

from exts import db

import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(common_bp)

    db.init_app(app)
    CSRFProtect(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
