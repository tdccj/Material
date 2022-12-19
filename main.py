# coding = utf-8
# 用于收集管理素材
# @tdccj

# 难以实现透明，已被放弃

import tkinter
from tkinter import *

version = "v0.1"


def set_main():
    # 设置主窗口
    mainWindow.title("素材管理 " + version)
    mainWindow.iconbitmap("logo_fang_1.ico")
    # 设置标题和logo
    mainWindow.geometry("250x300")
    mainWindow.minsize(125, 150)
    # 设置窗口大小 宽x高
    mainWindow.overrideredirect(True)
    # 设置无边框窗口
    mainWindow.wm_attributes("-topmost", True)
    # 设置窗口置顶
    mainWindow.config(bg="")


def set_bar():
    # 创建控制条
    bar_frame = tkinter.Frame(mainWindow)
    bar_frame.pack()
    off_button = tkinter.Button(bar_frame, text="off", command=off_main)    # 创建关闭键
    off_button.pack()


def off_main():
    mainWindow.destroy()


if __name__ == "__main__":
    mainWindow = Tk()

    set_main()
    set_bar()

    mainWindow.mainloop()
