#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
def loading():
    line = []
    text = ''
    zhailu = open('./zhailu.cau', 'r')
    for i in zhailu:
        for a in i:
            if a == '\n' or a == '|' or a == '':
                line.append(text)
                text = ''
            else:
                text = text + a
        sentence = []
        theme = []
        source = []
        author = []
        types = []
        means = []
        time = 0
        for c in line:
            time = time + 1
            if time == 7:
                time = 1
            elif time == 1:
                sentence.append(c)
            elif time == 2:
                theme.append(c)
            elif time == 3:
                source.append(c)
            elif time == 4:
                author.append(c)
            elif time == 5:
                types.append(c)
            elif time == 6:
                means.append(c)
    zhailu.close()
    return line
def save(a):
    the_list = loading() + a
    zhailu = open('zhailu.cau', 'w')
    sentences = []
    themes = []
    sources = []
    authors = []
    types = []
    means = []
    time = 0
    for i in the_list:
        time = time + 1
        if time == 7:
            time = 1
        if time == 1:
            sentences.append(i)
        elif time == 2:
            themes.append(i)
        elif time == 3:
            sources.append(i)
        elif time == 4:
            authors.append(i)
        elif time == 5:
            types.append(i)
        elif time == 6:
            means.append(i)
    for i in sentences:
        zhailu.write(i)
        zhailu.write('|' + themes[sentences.index(i)])
        zhailu.write('|' + sources[sentences.index(i)])
        zhailu.write('|' + authors[sentences.index(i)])
        zhailu.write('|' + types[sentences.index(i)])
        zhailu.write('|' + means[sentences.index(i)] + '\n')
    zhailu.close()


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
        self.master.geometry('1009x930')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        # 文本
        self.Text1Font = Font(font=('宋体',9))
        self.Text1 = Text(self.top, font=self.Text1Font)
        self.Text1.place(relx=0.024, rely=0.034, relwidth=0.929, relheight=0.259)

        # 意思
        self.Text5Font = Font(font=('宋体',9))
        self.Text5 = Text(self.top, font=self.Text5Font)
        self.Text5.place(relx=0.024, rely=0.559, relwidth=0.929, relheight=0.233)

        self.Text2Var = StringVar(value='主题')
        self.Text2 = Entry(self.top, text='主题', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.024, rely=0.318, relwidth=0.929, relheight=0.053)

        self.Text3Var = StringVar(value='作者')
        self.Text3 = Entry(self.top, text='作者', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.024, rely=0.447, relwidth=0.929, relheight=0.061)

        self.Text4Var = StringVar(value='出处')
        self.Text4 = Entry(self.top, text='出处', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.024, rely=0.378, relwidth=0.929, relheight=0.061)

        self.Combo1List = ['句子','词语','知识笔记']
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.024, rely=0.525, relwidth=0.929, relheight=0.022)
        self.Combo1.set(self.Combo1List[0])

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='Save', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.357, rely=0.809, relwidth=0.271, relheight=0.096)



class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        global InitList
        a = ''
        b = ''
        c = ''
        d = ''
        e = ''
        # Forbiding '\n' and backspace
        for i in self.Text1.get('0.0','end'):
            if i != ' ' and i != '\n':
                a = a + i
        if a in the_list:
            print('重复！')
        else:
            for i in self.Text2Var.get():
                if i != ' ' and i != '\n':
                    b = b + i
            for i in self.Text4Var.get():
                if i != ' ' and i != '\n':
                    c = c + i
            for i in self.Text3Var.get():
                if i != ' ' and i != '\n':
                    d = d + i
            for i in self.Text5.get('0.0','end'):
                if i != ' ' and i != '\n':
                    e = e + i
            lists=[a,b,c,d,self.Combo1.get(),e]
            InitList = lists
            save(InitList)
            print('finish')
            pass

if __name__ == "__main__":
    the_list = loading()
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass