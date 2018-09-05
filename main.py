#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""FTP服务器GUI"""

import os
import sys
from tkinter import (Button, Entry, Frame, Label, StringVar, Tk, filedialog, messagebox)

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer, ThreadedFTPServer

import _thread


class FTP(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("FTP服务器GUI")
        self.set_window_center(self, 300, 180)
        self.resizable(False, False)
        self.update()

        self.server = None
        self.server_thread = None
        self.running = StringVar(value="normal")
        self.var_username = StringVar(value="doudou")
        self.var_passwd = StringVar(value="doudou")
        self.var_address = StringVar(value="127.0.0.1")
        self.var_port = StringVar(value="3333")
        self.var_path = StringVar(value=".")  # 默认路径

        self.entry_username = None
        self.entry_passwd = None
        self.entry_address = None
        self.entry_port = None
        self.entry_path = None

        self.load_view()

    def run_ftp(self):
        if os.path.isdir(self.var_path.get()) is not True:
            messagebox.showerror(title="提示", message="路径不对", parent=self)
            return

        _thread.start_new_thread(self.ftpserver, ())
        self.fixed_entry("readonly")

    def stop_ftp(self):
        self.fixed_entry()
        if self.server:
            try:
                self.server.close()
            except Exception:
                print(Exception)

    def ftpserver(self):

        # 实例化虚拟用户，这是FTP验证首要条件
        authorizer = DummyAuthorizer()

        # 添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
        authorizer.add_user(
            self.var_username.get(),
            self.var_passwd.get(),
            self.var_path.get(),
            perm="elradfmwMT")

        # 添加匿名用户，任何人都可以访问，否则需要输入用户名和密码才能访问
        # 匿名用户只需要配置路径
        authorizer.add_anonymous(self.var_path.get(), msg_login="Welcome")

        # 初始化ftp句柄
        handler = FTPHandler
        handler.authorizer = authorizer

        # 监听ip和端口
        self.server = ThreadedFTPServer(
            (self.var_address.get(), self.var_port.get()), handler)

        # 开始服务
        self.server.serve_forever()

    def load_view(self):
        """界面"""

        Label(self, text="账号:").grid(column=0, row=0, sticky="nswe")
        self.entry_username = Entry(self, textvariable=self.var_username, bd=2)
        self.entry_username.grid(column=1, row=0, columnspan=2, sticky="nswe")

        Label(self, text="密码:").grid(column=0, row=1, sticky="nswe")
        self.entry_passwd = Entry(self, textvariable=self.var_passwd, bd=2)
        self.entry_passwd.grid(column=1, row=1, columnspan=2, sticky="nswe")

        Label(self, text="地址:").grid(column=0, row=2, sticky="nswe")
        self.entry_address = Entry(self, textvariable=self.var_address, bd=2)
        self.entry_address.grid(column=1, row=2, columnspan=2, sticky="nswe")

        Label(self, text="端口:").grid(column=0, row=3, sticky="nswe")
        self.entry_port = Entry(self, textvariable=self.var_port, bd=2)
        self.entry_port.grid(column=1, row=3, columnspan=2, sticky="nswe")

        Label(self, text="路径:").grid(column=0, row=4, sticky="nswe")
        self.entry_path = Entry(self, textvariable=self.var_path, bd=2)
        self.entry_path.grid(column=1, row=4)

        self.btn_select_path = Button(self, text="选择", command=self.selectPath)
        self.btn_select_path.grid(column=2, row=4)

        btn_box = Frame(self, relief="ridge", borderwidth=0, bd=2)
        btn_box.grid(column=0, row=5, columnspan=3, sticky="nswe")

        self.btn_start = Button(btn_box, text="启动", command=self.run_ftp)
        self.btn_start.pack(side="left")

        self.btn_stop = Button(
            btn_box, text="停止", command=self.stop_ftp, state="disable")
        self.btn_stop.pack(side="left")

    def selectPath(self):
        path = filedialog.askdirectory()
        if os.path.isdir(path):
            self.var_path.set(path)

    def fixed_entry(self, state="normal"):
        s = "readonly" if (state == "readonly") else "normal"
        a = "disable" if (state == "readonly") else "normal"
        self.entry_username["state"] = s
        self.entry_passwd["state"] = s
        self.entry_address["state"] = s
        self.entry_port["state"] = s
        self.entry_path["state"] = s
        self.btn_select_path["state"] = a
        self.btn_start["text"] = "运行中" if (state == "readonly") else "启动"
        self.btn_start["state"] = a
        self.btn_stop["state"] = "normal" if (
            state == "readonly") else "disable"

    def set_window_center(self, window, width, height):
        """设置窗口宽高及居中"""
        # 获取屏幕 宽、高
        w_s = window.winfo_screenwidth()
        h_s = window.winfo_screenheight()
        # 计算 x, y 位置
        x_co = (w_s - width) / 2
        y_co = (h_s - height) / 2 - 50
        window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
        window.minsize(width, height)


if __name__ == "__main__":
    ftp = FTP()
    ftp.mainloop()
