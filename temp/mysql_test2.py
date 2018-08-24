import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="39.106.121.185", user="root",
                     password="!QAZ@WSx", db="trading_ua", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from t_user WHERE trader_id = '00000024537'"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("trader_id", "name", "phone")
    # 遍历结果
    for row in results:
        trader_id = row[0]
        name = row[1]
        phone = row[14]
        print(trader_id, name, phone)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接
