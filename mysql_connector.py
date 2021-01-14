#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/14 下午4:07
# @Author: Bruce Chen
# @Site: 
# @File: mysql_connector.py
# @Software: PyCharm

import pymysql

db = pymysql.connect(host="10.103.64.212", port=3307, user="sandbox", password="password", db="sandbox", charset='utf8')
cursor = db.cursor()
sql = "SELECT * FROM report_schedule"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        report_title = row[1]
        mail_to = row[2]
        repeat_type = row[3]
        device_list = row[4]
        create_time = row[5]
        modify_time = row[6]
        next_run_time = row[7]
        print(id, report_title, mail_to, report_title, device_list, create_time, modify_time, next_run_time)
except:
    print("Error")

db.close()