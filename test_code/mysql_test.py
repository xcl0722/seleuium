# -*- coding: utf-8 -*-
"""python版本3.8.3
改脚本通过ssh连接到测试主机  使用sysbench 工具 执行命令进行基准测试
"""
import pymysql
import datetime
import paramiko,os,time,re
class Mysql_Test:
    def connect_verify(self,host,port,user,password):


        try:
            con=pymysql.connect(host=host,port=port,user=user,password=password,database='mysql',charset='utf8')
        except:
            print('连接mysql失败，请检查mysql服务或网络！')
            os._exit(0)
    def basic_connect(self,ip,port,username,password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, port, username, password)
            return ssh
        except:
            print('连接测试客户端失败！请检查网络或账密！')
            os._exit(0)

    def default_test(self,ssh):
        # 测试mysql基本信息
        mysql_ip = '10.67.40.87'
        mysql_port = 33306
        mysql_user = 'root'
        mysql_password = 'ROJeST0ayMc1'
        self.connect_verify(mysql_ip,mysql_port,mysql_user,mysql_password)#验证mysql
        #默认测试数据
        param_list=[{'table_count':1,'table_size':10000,'threads':24},
                    {'table_count':1,'table_size':10000,'threads':48},
                    {'table_count':1,'table_size':10000,'threads':72},
                    {'table_count':1,'table_size':10000,'threads':96},
                    {'table_count':1,'table_size':10000,'threads':120},
                    {'table_count':1,'table_size':10000,'threads':144},
                    {'table_count':1,'table_size':10000,'threads':168},
                    {'table_count':1,'table_size':10000,'threads':192},
                    {'table_count':1,'table_size':10000,'threads':256},
                    {'table_count':1,'table_size':10000,'threads':512},
                    {'table_count':1,'table_size':10000,'threads':1024},
                   ]
        # 报告路径
        test_log_name = 'mysql_default_test.log'
        test_log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), test_log_name)
        test_log_path = open(test_log_path, 'a')
        # 开始测试，生成报告
        print("测试中请稍后。。。")
        print('******************测试报告******************', file=test_log_path)
        print("测试时间：", datetime.datetime.now(), file=test_log_path)
        print("测试数据库", mysql_ip, file=test_log_path)
        for i in param_list:
            #准备测试数据
            stdin, stdout_mysql, stderr=ssh.exec_command('sysbench /usr/local/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host={} --mysql-port={} --mysql-user={} --mysql-password={} --oltp-test-mode=complex --oltp-tables-count=1 --oltp-table-size=10000 --threads=10 --time=120 --report-interval=30 prepare'.format(mysql_ip,mysql_port,mysql_user,mysql_password))
            result = stdout_mysql.read().decode('utf8')
            #开始测试
            stdin, stdout_mysql, stderr=ssh.exec_command('sysbench /usr/local/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host={} --mysql-port={} --mysql-user={} --mysql-password={} --oltp-test-mode=complex --oltp-tables-count=1 --oltp-table-size=10000 --threads=10 --time=120 --report-interval=30 run'.format(mysql_ip,mysql_port,mysql_user,mysql_password))
            result_mysql=stdout_mysql.read().decode('utf8')
            tps=re.search("transactions.*?\n",result_mysql).group(0)
            qps=re.search("queries:.*?\n",result_mysql).group(0)
            nine_five_th=re.search("95th percentile.*?\n",result_mysql).group(0)
            #清除测试数据
            stdin, stdout_mysql, stderr=ssh.exec_command('sysbench /usr/local/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host={} --mysql-port={} --mysql-user={} --mysql-password={} --oltp-test-mode=complex --oltp-tables-count=1 --oltp-table-size=10000 --threads=10 --time=120 --report-interval=30 cleanup'.format(mysql_ip,mysql_port,mysql_user,mysql_password))
            result = stdout_mysql.read().decode('utf8')
            print("测试参数：表数量{} 每张表记录{} 并发数{} 测试时间120s".format(i['table_count'],i['table_size'],i['threads']), file=test_log_path)
            print('TPS：'+ tps+'\n'+'QPS：'+qps+'\n'+'95th：'+nine_five_th, file=test_log_path)
        print("测试完成请检查测试报告！")
    def custom(self,ssh):
        # 测试mysql基本信息
        mysql_ip = '10.67.40.87'
        mysql_port = 33306
        mysql_user = 'root'
        mysql_password = 'ROJeST0ayMc1'
        self.connect_verify(mysql_ip, mysql_port, mysql_user, mysql_password)  # 验证mysql
        #测试数据 按需增添
        param_list = [{'table_count': 1, 'table_size': 10000, 'threads': 10},
                      ]
        # 报告路径
        test_log_name = 'mysql_default_test.log'
        test_log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), test_log_name)
        test_log_path = open(test_log_path, 'a')
        # 开始测试，生成报告
        print("测试中请稍后。。。")
        print('******************测试报告******************', file=test_log_path)
        print("测试时间：", datetime.datetime.now(), file=test_log_path)
        print("测试数据库", mysql_ip, file=test_log_path)
        for i in param_list:
            # 准备测试数据
            stdin, stdout_mysql, stderr = ssh.exec_command(
                'sysbench /usr/local/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host={} --mysql-port={} --mysql-user={} --mysql-password={} --oltp-test-mode=complex --oltp-tables-count=1 --oltp-table-size=10000 --threads=10 --time=120 --report-interval=30 prepare'.format(
                    mysql_ip, mysql_port, mysql_user, mysql_password))
            result = stdout_mysql.read().decode('utf8')
            # 开始测试
            stdin, stdout_mysql, stderr = ssh.exec_command(
                'sysbench /usr/local/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host={} --mysql-port={} --mysql-user={} --mysql-password={} --oltp-test-mode=complex --oltp-tables-count=1 --oltp-table-size=10000 --threads=10 --time=120 --report-interval=30 run'.format(
                    mysql_ip, mysql_port, mysql_user, mysql_password))
            result_mysql = stdout_mysql.read().decode('utf8')
            tps = re.search("transactions.*?\n", result_mysql).group(0)
            qps = re.search("queries.*?\n", result_mysql).group(0)
            nine_five_th = re.search("95th percentile.*?\n", result_mysql).group(0)
            # 清除测试数据
            stdin, stdout_mysql, stderr = ssh.exec_command(
                'sysbench /usr/local/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host={} --mysql-port={} --mysql-user={} --mysql-password={} --oltp-test-mode=complex --oltp-tables-count=1 --oltp-table-size=10000 --threads=10 --time=120 --report-interval=30 cleanup'.format(
                    mysql_ip, mysql_port, mysql_user, mysql_password))
            result = stdout_mysql.read().decode('utf8')
            print("测试参数：表数量{} 每张表记录{} 并发数{} 测试时间120s".format(i['table_count'], i['table_size'], i['threads']),
                  file=test_log_path)
            print('TPS:' + tps + '\n' + 'QPS:' + qps + '\n' + '95th' + nine_five_th, file=test_log_path)
        print("结束时间：", datetime.datetime.now(), file=test_log_path)
        print("测试完成请检查测试报告！")
class Fio_Test:
    def test1(self):
        print("fio待补充")

if __name__ =='__main__':
    test=Mysql_Test()
    ssh_con=test.basic_connect('10.67.40.126',22,'root','lxd19970529')#测试终端
    #默认测试
    test.default_test(ssh_con)
    #自定义测试
    #test.custom(ssh_con)


