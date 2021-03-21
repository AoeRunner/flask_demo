# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/21 20:04
# @Author:汤易怀
# @File  :emp.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import json

from flask import Blueprint
import db.emp

emp = Blueprint("emp_data", __name__)


@emp.route("/emp/search_emp_list")
def search_emp_list():
    lists = db.emp.search_emp_list()
    lists = str(lists)
    return lists
