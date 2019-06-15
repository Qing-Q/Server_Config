#!/usr/bin/env python3
#coding:utf-8


from lib import commands_
from lib import commands__
from lib import root
from lib import info
from lib import warning
from lib import error
from lib import print_
from lib import argparse_
from lib.sftp_server import Config as sftp_config


c1 = commands_(cmd=['sudo chmod +x {}lib/File_content_clear && {}lib/File_content_clear'.format(root,root)])
warning(c1)






def main():
    args = argparse_()
    sftp = args.sFtp_config
    if sftp:
        config = sftp_config()
        config.main()
        info('SFTP 服务配置完毕.')





if __name__ == "__main__":
    main()

