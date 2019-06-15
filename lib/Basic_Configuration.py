#!/usr/bin/env python3
#coding:utf-8

from .__init__ import commands_
from .__init__ import commands__



def add_user_group(group_name,path,username):
    """
    创建用户 和 组 
    """
    cmd1 = 'sudo groupadd {}'.format(group_name)
    cmd2 = 'sudo useradd -g {} -s {} {}'.format(group_name,path,username)
    cmd3 = 'sudo mkpasswd {}'.format(username)
    cmd4 = 'sudo passwd {}'.format(username)

    commands__(cmd1)
    commands__(cmd2)
    commands__(cmd3)
    commands__(cmd4)


def add_Catalog(path,name):
    """
    新建目录.
    """
    cmd1 = 'sudo mkdir {}{}'.format(path,name)
    commands__(cmd1)

def add_File(path,name):
    """
    新建文件.
    """
    cmd1 = 'sudo touch {}{}'.format(path,name)
    commands__(cmd1)

def cP_Catalog(source_path,target_path):
    """
    复制目录.
    """
    cmd1 = 'sudo cp -v -r {} {}'.format(source_path,target_path)
    commands__(cmd1)

def cP_File(source_name,target_name):
    """
    复制文件.
    """
    cmd1 = 'sudo cp -v {} {}'.format(source_name,target_name)
    commands__(cmd1)


def conFig_File_Permissions(pErmissions,name):
    """
    配置文件权限.
    """
    cmd1 = 'sudo chmod {} {}'.format(pErmissions,name)
    commands__(cmd1)


def conFig_Catalog_Permissions(pErmissions,path):
    """
    配置目录权限.
    """
    cmd1 = 'sudo chmod {} -R {}'.format(pErmissions,path)
    commands__(cmd1)


def delete_user(name):
    """
    删除用户
    """
    cmd1 = 'sudo userdel -f {}'.format(name)
    commands__(cmd1)

def set_Owner(name,path):
    """
    添加属主
    """
    cmd1 = 'sudo chown root:{} {}'.format(name,path)

def conFig_Catalog_Permissions_1(group,name,path):
    """
    设置目录权限 chown
    """
    cmd1 = 'sudo chown {}:{} {}'.format(group,name,path)
    commands__(cmd1)


