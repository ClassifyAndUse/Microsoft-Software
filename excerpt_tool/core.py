import os,sys
def laoding():
    line = []
    time = 0
    text = ''
    zhailu = open('./zhailu.file','r')
    for i in zhailu:
        for a in i:
            if a == '\n' or a == '|' or a == '':
                line.append(text)
                text = ''
            else:
                text = text + a
    zhailu.close()
    return line
def Search(keyword,theme,source,author,the_list):
    sentence = []
    theme = []
    source = []
    author = []
    for c in the_list:
            time = time + 1
            if time == 5:
                time = 1
            elif time == 1:
                sentence.append(c)
            elif time == 2:
                theme.append(c)
            elif time == 3:
                source.append(c)
            elif time == 4:
                author.append(c)
    if keyword != '':
        for i in sentence:
            if keyword in i:
                id = sentence.index(i)
    print('[句子]'+sentence[id])
    print('[主题]'+theme[id])
    print('[出处]'+source[id])
    print('[作者]'+author[id])
def add(the_list,):
    zhailu1 = open('zhailu1.file','w')
    while True:
        sentence = input('[句子]')
        if sentence == '':
            zhailu1.close()
            break
        zhailu1.write(sentence)
        zhailu1.write('|'+input('[主题]'))
        zhailu1.write('|'+input('[出处]'))
        zhailu1.write('|'+input('[作者]'))
def save():
    is_exit = input("是否退出[y/n]：")
    if is_exit == 'y':
        os.rename('zhailu1.file','zhailu.file')