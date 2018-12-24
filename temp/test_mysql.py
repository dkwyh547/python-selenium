#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = INSERT INTO EMPLOYEE(trader_id, status, trader_type,password, id_card, id_card_image_address1, id_card_image_address2, email, name, register_date, detail_addr, address, post_no,phone, rec_firm, trade_status, lock_withdraw, lock_income, lock_buy, lock_sell, id_card_image_p, id_card_image_b, month_setting_fee, month_surplus_fee, sub_team, create_time, modify_time, version, last_ip, last_login_time, bank_return_msg, bank_return_no)
VALUES ("70000000012", "10", "c", "11f5b88265b6b69a456da1c4c3ac0ca6", "430224198909081227", "/uploads/2017-09-30/1954010b-fed3-4e23-b0a9-7fdc9ec7d95e.jpg", "/uploads/2017-09-30/403472a0-fab6-4a28-8539-6d381b457251.jpg", "null", "周莉琪", "null", "null", "null", "null", "13898176543", "null", "0", "0", "0", "0", "0", "null", "null", "-1", "0", "700", "2017/10/20 17:45", "2018/10/19 13:17", "26529", "未知", "1539926257131", "null", "null")

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()