import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="10.65.5.99", user="kircp",
                     password="kircp!2K8", db="kircp", port=3307)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql = "INSERT INTO 'kircp'.'ers_bjjl' (`id`,`bjdh`,`jzxm`,`ssqh`,`bjkssj`,`created_by`,`created_time`,`updated_by`," \
      "`updated_time`) VALUES ('01ee39e2-cd8e-4330-afb7-82fea0da7c44', '17751237533', 'xuxu2020', '苏州', '2020-10-12 " \
      "20:31:39', 'ers-admin', 'ers-admin', '2020-10-12 20:31:40')"  # sql语句

cur.execute(sql)
# 提交
db.commit()

db.close()
