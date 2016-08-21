# -*- coding: utf-8 -*-
import mysql.connector
# 创建连接
config = {
          'user':'root',
          'password':'888888',
          'host':'127.0.0.1',
          'port':3306,
          'database':'sakila'}
conn = mysql.connector.connect(**config)

# 创建游标
cur = conn.cursor()

# 执行查询SQL
sql = "SELECT * from actor"
cur.execute(sql)

# 获取查询结果
result_set = cur.fetchall()
if result_set:
    for row in result_set:
        print row[0]
        print row

# 关闭游标和连接
cur.close()
conn.close()




