#coding=utf-8
import os
import paramiko

class LinuxOrder:
    def connect(self):
        try:
            self.ip = "192.168.7.83"
            self.port = 22
            self.username = "root"
            self.password = "kedacom888"
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.username, self.password)
            print('{0}：连接成功'.format(self.ip))
        except Exception as e:
            print('{0}：连接失败'.format(self.ip))
            raise e

    def ssh_exec_cmd(self, cmd, path='~'):
        """
        通过ssh连接到远程服务器，执行给定的命令
        :param cmd: 执行的命令
        :param path: 命令执行的目录
        :return: 返回结果
        """
        try:
            result = self._exec_command('cd ' + path + ';' + cmd)
            print(result)
        except Exception:
            raise RuntimeError('exec cmd [%s] failed' % cmd)


    def close_ssh(self):
        """关闭ssh连接"""
        self.ssh.close()
        print('关闭ssh连接')

    def _exec_command(self, param):
        pass


if __name__ == '__main__':
    L = LinuxOrder()
    L.connect()
    L.ssh_exec_cmd('cd ' + 'sipp-3.3.990' + ';' + 'sh uac_sendbye.sh 17751237537 1009 5080')
    L.close_ssh()