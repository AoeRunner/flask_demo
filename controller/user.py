# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/21 17:24
# @Author:汤易怀
# @File  :user.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from flask import Blueprint

user = Blueprint("user", __name__)


@user.route("/user/login")
def login():
    return "登录成功"
