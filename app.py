# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/18 21:35
# @Author:汤易怀
# @File  :app.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from flask import Flask, render_template

from controller.user import user

app = Flask(__name__)
app.register_blueprint(user)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route("/welcome")
def welcome():
    return render_template("welcome.html", message="asdas das")


if __name__ == '__main__':
    app.run()
