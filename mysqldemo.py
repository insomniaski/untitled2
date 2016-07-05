# -*- coding: utf-8 -*-
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Pass@word',
                             db='clctdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `testtable` (`id`, `name`) VALUES (%s, %s)"
        # cursor.execute(sql, ('123', '测试'))
        sql = "INSERT INTO `demotable` (`id`, `name`) VALUES ('test', '测试2')"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `testtable` "
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
