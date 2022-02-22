#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from os.path import join
from tkinter import Label, Toplevel
from tkinter.font import Font
from webbrowser import open as url_open

import utils.global_variable as glv
from utils.functions import set_window_center


class WinAbout(Toplevel):
    '''关于窗口'''

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.title('关于')
        # 依附主窗体
        self.transient(master)
        # 设置大小位置
        set_window_center(self, 260, 160)

        # self.img = join(glv.get_item('APP_PATH'), glv.get_item('DATA_DIR'), 'image', 'logo_about.png')
        # self.logo = PhotoImage(width=64, height=64, file=self.img)
        # Label(self, image=self.logo, width=64, height=80).pack()
        Label(self,
              text=glv.get_item('APP_DISPLAY_NAME'),
              pady=10,
              font=Font(size=15, weight='bold')).pack()

        Label(self,
              text='版本: %s' % glv.get_item('APP_VERSION'),
              font=Font(size=13)).pack()
        Label(self, text='', pady=1).pack()

        site = Label(self,
                     text='官方网站',
                     cursor='hand',
                     font=Font(size=11, underline=True))
        site.bind('<Button-1>', self.open_site)
        site.pack()

        Label(self, text=glv.get_item('APP_COPYRIGHT'),
              font=Font(size=10)).pack()
        Label(self, text='All rights reserved.', font=Font(size=10)).pack()

    def open_site(self, _):
        url_open(glv.get_item('APP_SITE'), new=0)


if __name__ == '__main__':
    app = WinAbout()
    app.mainloop()
