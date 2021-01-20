# -*- coding: utf-8 -*-
"""python版本3.8.3
改脚本通过ssh连接到测试主机  使用kafka自带脚本进行测试   测试主机需安装好kafka自带的脚本"""
from kafka import KafkaProducer
import os,paramiko,time,datetime,json
class Es_Test:
    def connect_verify(self,kafka_ip,kafka_port):
        try:
            producer = KafkaProducer(
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                bootstrap_servers=['10.67.40.87:19092']
            )

        except:
            print("连接kafka失败，请检查kafka服务或网络！")
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
        #es基本信息
        kafka_ip='10.67.40.87'
        kafka_port=19092
        self.connect_verify(kafka_ip,kafka_port)#验证es
        #参数解析
        topic = "test"  # topic名称
        # num_records = 10000  # 总共需要发送的消息数
        # record_size = 1024  # 每个记录的字节数
        # throughput = 1000  # 每秒钟发送的记录数
        # fetch_size = 1048576  # 指定每次fetch的数据的字节大小 1k
        # messages = 10000  # 总共要消费的消息数
        # threads = 1  # 并发数
        param_list=[{'num_records':10000,'record_size':1024,'throughput':2000,'fetch_size':1048576,'messages':10000,'threads':1},
                    {'num_records':100000,'record_size':1024,'throughput':2000,'fetch_size':1048576,'messages':100000,'threads':1},
                    {'num_records':1000000,'record_size':2048,'throughput':5000,'fetch_size':1048576,'messages':1000000,'threads':1},
                   # {'num_records':10000000,'record_size':2048,'throughput':5000,'fetch_size':1048576,'messages':10000000,'threads':1},
                    ]
        # 报告路径
        test_log_name = 'kafka_default_test.log'
        test_log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), test_log_name)
        test_log_path = open(test_log_path, 'a')
        # 开始测试生成报告
        print("测试中请稍后。。。")
        print('******************测试报告******************', file=test_log_path)
        print("测试时间：", datetime.datetime.now(), file=test_log_path)
        print("测试对象", kafka_ip, file=test_log_path)
        for i in param_list:
            stdin, stdout_kafka, stderr = ssh.exec_command("bash -l -c '/opt/kafka_2.12-2.5.1/bin/kafka-producer-perf-test.sh --topic {} --num-records {} --record-size {} --throughput {} --producer-props bootstrap.servers={}:{}'".format(topic,i['num_records'],i['record_size'],i['throughput'],kafka_ip,kafka_port),get_pty=True)
            kafka_result_pro=stdout_kafka.read().decode('utf8')

            stdin, stdout_kafka, stderr = ssh.exec_command("bash -l -c '/opt/kafka_2.12-2.5.1/bin/kafka-consumer-perf-test.sh --broker-list {}:{} --topic {} --fetch-size {} --messages {} --threads {}'".format(kafka_ip,kafka_port,topic,i['fetch_size'],i['messages'],i['threads']),get_pty=True)
            kafka_result_con=stdout_kafka.read().decode('utf8')
            print("测试参数：numrecords{} record_size{} throughput{} fetch_size{} messages{} threads{}".format(i['num_records'],i['record_size'],i['throughput'],i['fetch_size'],i['messages'],i['threads']),file=test_log_path)
            print("测试结果：",'\n'+"生产者："+'\n'+kafka_result_pro+'\n'+"消费者："+'\n'+kafka_result_con, file=test_log_path)
        print("结束时间:",datetime.datetime.now(),file=test_log_path)
        print("测试完成请检查测试报告！")
    def custom_test(self,ssh):
        #es基本信息
        kafka_ip='10.67.40.87'
        kafka_port=19092
        self.connect_verify(kafka_ip,kafka_port)#验证es
        #参数解析
        topic = "test"  # topic名称
        # num_records = 10000  # 总共需要发送的消息数
        # record_size = 1024  # 每个记录的字节数
        # throughput = 1000  # 每秒钟发送的记录数
        # fetch_size = 1048576  # 指定每次fetch的数据的字节大小 1k
        # messages = 10000  # 总共要消费的消息数
        # threads = 1  # 并发数
        #根据需求更改，增加
        param_list=[{'num_records':10000,'record_size':1024,'throughput':2000,'fetch_size':1048576,'messages':10000,'threads':1},

                    ]
        # 报告路径
        test_log_name = 'kafka_default_test.log'
        test_log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), test_log_name)
        test_log_path = open(test_log_path, 'a')
        # 开始测试生成报告
        print("测试中请稍后。。。")
        print('******************测试报告******************', file=test_log_path)
        print("测试时间：", datetime.datetime.now(), file=test_log_path)
        print("测试对象", kafka_ip, file=test_log_path)
        for i in param_list:
            stdin, stdout_kafka, stderr = ssh.exec_command("bash -l -c '/opt/kafka_2.12-2.5.1/bin/kafka-producer-perf-test.sh --topic {} --num-records {} --record-size {} --throughput {} --producer-props bootstrap.servers={}:{}'".format(topic,i['num_records'],i['record_size'],i['throughput'],kafka_ip,kafka_port),get_pty=True)
            kafka_result_pro=stdout_kafka.read().decode('utf8')
            print(kafka_result_pro)
            stdin, stdout_kafka, stderr = ssh.exec_command("bash -l -c '/opt/kafka_2.12-2.5.1/bin/kafka-consumer-perf-test.sh --broker-list {}:{} --topic {} --fetch-size {} --messages {} --threads {}'".format(kafka_ip,kafka_port,topic,i['fetch_size'],i['messages'],i['threads']),get_pty=True)
            kafka_result_con=stdout_kafka.read().decode('utf8')
            print(kafka_result_con)
            print("测试结果：",'\n'+"生产者："+'\n'+kafka_result_pro+'\n'+"消费者："+'\n'+kafka_result_con, file=test_log_path)
        print("测试完成请检查测试报告！")
class Fio_Test:
    def test1(self):
        print("fio待补充")
if __name__ == '__main__':
    test = Es_Test()
    ssh_con = test.basic_connect('10.67.40.126', 22, 'root', 'lxd19970529')  # 测试终端
    # 默认测试
    test.default_test(ssh_con)
    # 自定义测试
    #test.custom_test(ssh_con)