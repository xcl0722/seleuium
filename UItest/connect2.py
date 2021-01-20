# -*- coding: utf-8 -*-
import time

import paramiko

client = paramiko.SSHClient()# 实例化SSHClient

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接

client.connect(hostname='192.168.7.83', port=22, username='root', password='kedacom888')# 连接SSH服务端，以用户名和密码进行认证

# 打开一个Channel并执行命令
time.sleep(3)
stdin, stdout, stderr = client.exec_command('sh start_xu.sh')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
# print("666")
# 打印执行结果
print(stdout.read().decode('utf-8'))
# 关闭SSHClient
client.close()
