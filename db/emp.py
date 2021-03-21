# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/21 20:09
# @Author:汤易怀
# @File  :emp.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from db.mysql import Session


def search_emp_list():
    session = Session()
    sql = '''
        SELECT * FROM t_emp
    '''
    cursor = session.execute(sql)
    result = cursor.fetchall()
    print(result)
    session.close()
    return result