# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/21 20:04
# @Author:汤易怀
# @File  :emp_data.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from flask import Blueprint
import db.emp_data

emp_data = Blueprint("emp_data", __name__)


@emp_data.route("/emp/search_emp_list")
def search_emp_list():
    lists = db.emp_data.search_emp_list()
    return lists
