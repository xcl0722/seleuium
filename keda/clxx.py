#!/usr/bin/python3
import pymysql
import configparser
import os
import uuid
import datetime
import random
config = configparser.ConfigParser()
root_path = os.path.dirname(os.path.abspath(__file__))
config.read(root_path+"/config/system.ini", encoding='utf-8')
print("根目录", root_path)
print("所有节点==>", config.sections())
# mysql 实例
class MysqlClient():
    def __init__(self, database, hostname, user, password, port):
        self._conn = pymysql.connect(
            host=hostname, user=user, password=password,  port=port, database=database)
        self.cursor = self._conn.cursor()
        print('connect successful!')
    # query methods
    def queryAll(self, sql,):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def updateBy(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
            self._conn.commit()
            return
        else:
            self.cursor.execute(sql)

    def queryOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

# 读取配置文件
def getConfig(env):
    print("输出元组，包括option的key和value", config.items(env))
    return dict(config.items(env))

# 保存至车辆信息
def saveData(env):
    conf = getConfig(env)
    client = MysqlClient(conf['database'], conf['hostname'], conf['user'],
                         conf['password'], int(conf['port']))
    # 支队编号
    zdbh = conf['zdbh']
    jgxxIdList = client.queryAll(
        "select id from ers_jgxx where jgjb='4' and jgnbbh like '%{}%'  UNION  all SELECT id from ers_jgxx where jgjb='5' and jgnbbh like '%{}%'  ".format(zdbh, zdbh))
    clsm = int(conf['clsm'])
    car_prefix = conf['car_prefix']
    car_suffix = conf['car_suffix']
    cllx = conf['cllx']
    xfclx = conf['xfclx']
    cldj = conf['cldj']
    zzgn = conf['zzgn']
    createId = conf['createid']
    clzt = conf['clzt']
    sdcd = conf['sdcd']
    cllxcount = int(conf['cllxcount'])
    xfclxcount = int(conf['xfclxcount'])
    # 车辆类型
    cllxSql = "select no from ers_code_item where code_type_no= '{}' ".format(
        cllx)
    cllxNo = client.queryAll(cllxSql)
    # 消防车类型
    xfclxSql = "select no from ers_code_item where code_type_no= '{}' and parent_no='21010000' ".format(
        xfclx)
    xfclxNo = client.queryAll(xfclxSql)
    # 待插入表
    insertSql = 'INSERT INTO `kircp`.`ers_clxx`(`id`, `jgbh`, `cphm`,  `cllx`, `xfclx`, `cldj`, `zzgn`, `zzsrl`, `zzpml`, `sdcd`, `clzt`,\
             `created_by`,  `created_time`, `updated_by`, `updated_time`) values(%(id)s, %(jgbh)s, %(cphm)s,  %(cllx)s, %(xfclx)s, %(cldj)s, \
             %(zzgn)s,%(zzsrl)s, %(zzpml)s, %(sdcd)s,%(clzt)s, %(created_by)s, %(created_time)s, %(updated_by)s, %(updated_time)s)'
    print("开始插入{}车辆信息".format(car_prefix))
    for jgbh in jgxxIdList:
        for num in range(0, clsm):
            clcount = random.randint(0, cllxcount)
            xfcount = random.randint(0, xfclxcount)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            client.updateBy(insertSql, {
                "id": str(uuid.uuid4()),
                "jgbh": jgbh,
                "cphm": car_prefix + datetime.datetime.now().strftime('%H%M%S%f')[2:9] + car_suffix,
                "cllx": cllxNo[clcount][0],
                "xfclx": xfclxNo[xfcount][0],
                "cldj": cldj,
                "zzgn": zzgn,
                "zzsrl": "5",
                "zzpml": "20",
                "sdcd": sdcd,
                "clzt": clzt,
                "created_by": createId,
                "created_time": now,
                "updated_by": createId,
                "updated_time": now
            })
    print("插入成功:{}".format(car_prefix))


if __name__ == "__main__":
    sections = config.sections()
    for env in sections:
        saveData(env)
