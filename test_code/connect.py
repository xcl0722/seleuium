#coding=utf-8
import paramiko
try:
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('192.168.7.83',22,'root','kedacom888')
    std_in,std_out,std_err = ssh_client.exec_command('cd /root/sipp-3.3.990/;sh uac_sendbye.sh 17751237537 1009 5080',get_pty=True)
    # 在command命令最后加上 get_pty=True，执行多条命令 的话用；隔开，另外所有命令都在一个大的单引号范围内引用
    std_in.write('PWD'+'\n') #执行输入命令，输入sudo命令的密码，会自动执行
    for line in std_out:
        print (line.strip('\n'))
    ssh_client.close()
except:
    print()