#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DouFTP Server"""

from multiprocessing import Process, freeze_support
from os.path import dirname

import utils.global_variable as g
from app import App

# 全局变量
g.init()
g.set_item('APP_NAME', 'DouFTP Server')
g.set_item('APP_BOUNDLE_ID', 'org.douftp.server.desktop')
g.set_item('APP_DISPLAY_NAME', 'DouFTP Server 桌面端')
g.set_item('APP_VERSION', '0.0.1')
g.set_item('APP_COPYRIGHT', 'Copyright © 2018-2022 Crogram Inc.')
g.set_item('APP_PATH', dirname(__file__))  # 当前目录
# g.set_item('DATA_DIR', 'data')
g.set_item('APP_SITE', 'https://douftp.org?utm_source=desktop_server&version=0.0.1')


if __name__ == "__main__":
    freeze_support()
    Process(target=App).start()
    # App()
