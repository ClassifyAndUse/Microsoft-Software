#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
import api
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('780x602')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Combo1List = ['句子','词语','笔记']
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.041, rely=0.279, relwidth=0.873, relheight=0.033)
        self.Combo1.set(self.Combo1List[0])

        self.Text1Var = StringVar(value='文字')
        self.Text1 = Entry(self.top, text='文字', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.041, rely=0.053, relwidth=0.883, relheight=0.188)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='save', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.4, rely=0.89, relwidth=0.206, relheight=0.068)

        self.Text2Var = StringVar(value='出处')
        self.Text2 = Entry(self.top, text='出处', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.041, rely=0.346, relwidth=0.883, relheight=0.042)

        self.Text3Var = StringVar(value='作者')
        self.Text3 = Entry(self.top, text='作者', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.041, rely=0.412, relwidth=0.883, relheight=0.068)

        self.Text4Var = StringVar(value='意思')
        self.Text4 = Entry(self.top, text='意思', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.041, rely=0.505, relwidth=0.894, relheight=0.254)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        #api.write(self.Text1Var['Text'])
        print(self.Text1Var['Text'])
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
