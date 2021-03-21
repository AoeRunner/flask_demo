# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/21 20:13
# @Author:汤易怀
# @File  :base_mysql.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
url = "mysql+mysqlconnector://root:abc123456@106.75.190.11:3306/test"
engine = create_engine(url, pool_size=5)
Session = sessionmaker(build=engine)