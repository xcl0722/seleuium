#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import random
import string
import uuid


# 定义要执行的SQL语句
count = 0
while (count < 5):
    db = pymysql.connect(host="10.65.5.99", user="kircp", password="kircp!2K8", db="kircp", port=3307)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    count = count+1
    id = uuid.uuid1()
    #   需要插入数据的数据要唯一性的都加循环数字
    #   新增的SQL语句，用format来替换我们的参数。
    sql = """
     INSERT INTO `kircp`.`ers_jqxx` (
    `id`,
    `jqbh`,
    `jqmc`,
    `jqlx`,
    `jqlb`,
    `jqdj`,
    `jqzt`,
    `ztmc`,
    `jyqk`,
    `jqbslbdm`,
    `gldwbh`,
    `gldwmc`,
    'bkrs',
    `cjyj`,
    `gxdw`,
    `sfdz`,
    `lc`,
    `jd`,
    'wd',
    'ssjg',
    'jjrbh',
    'jjrxm',
    'hbzt',
    'gljqbh',
    'sfjj',
    'bjjl_id',
    'mbxx_id',
    'mbzdynr',
    'lasj',
    'is_deleted',
    `created_by`,
    `created_time`,
    `updated_by`,
    `updated_time` 
)
VALUES
    (
        '{0}',
        NULL,
        '17799999999',
        'xuxuxu2020',
        'suzhou',
        NULL,
        NULL,
        NULL,
        '2020-10-15 09:51:19',
        NULL,
        NULL,
        NULL,
        NULL,
        'ers-admin',
        '2020-10-15 09:51:19',
        'ers-admin',
        '2020-10-15 09:53:19'
        '{0}',
        NULL,
        '19999999999',
        'xuxuxu2020',
        'suzhou',
        NULL,
        NULL,
        NULL,
        '2020-10-15 09:51:19',
        NULL,
        NULL,
        NULL,
        NULL,
        'ers-admin',
        '2020-10-15 09:51:19',
        'ers-admin',
        '2020-10-15 09:53:19'
    );
     """.format(id)
    # 执行SQL语句
    cursor.execute(sql)
    db.commit()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    #print("插入一条数据！")
    db.close()
print("end")