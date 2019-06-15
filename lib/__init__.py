#!/usr/bin/env python3
#coding:utf-8

__all__ = ['test','commands_',
           'info','error',
           'warning','print_',
           'AttribDict','load',
           'loads','dump',
           'dumps','root',
           'commands__',
           'modify','argparse_']


import random
import subprocess
import argparse
# import sys
from json import load
from json import loads
from json import dump
from json import dumps
from .debug import test
from .debug import log
from .datatype import AttribDict



# sys.dont_write_bytecode = True
info = log.info
error = log.error
warning = log.warning



W = '\033[0m'

G = '\033[1;32m'
O = '\033[1;33m'
R = '\033[1;31m'
B = '\033[1;34m'

root_ = subprocess.check_output('echo $HOME',shell=True).decode().strip()
root = '{}/.Tools/Server_Config/'.format(root_)
modify = '{}/.Tools/Server_Config/modify/'.format(root_)


def print_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    print(color+content+W)


def commands_(cmd=[],decodes_='utf-8'):
        """
            这是一个命令行解析方法.
            return <content or False>
        """
        try:
            cc = []
            c = subprocess.check_output(cmd,shell=True)
            c = c.decode(decodes_).strip()
            cc.append(c)
            for value in cc:
                if value:
                    return value
                else:
                    return False
        except Exception as e:
            # print_(traceback.format_exc())
            return False    
        

def commands__(cmd='',decodes_='utf-8'):
    """
        这是一个命令解析方法.
        return <True or False>
    """
    try:
        c = subprocess.call(cmd,shell=True)
        if int(c) == 0:
            return True
        else:
            return False
    except Exception as e:
        # print_(traceback.format_exc())
        return False


def argparse_():
    parser = argparse.ArgumentParser(description='服务器自动化配置工具.')
    parser.add_argument('--version','-v',action='store_true',help='查看版本.')
    parser.add_argument('--sFtp_config','-sftp',action='store_true',help='配置sftp服务器.')

    args = parser.parse_args()

    return args

    