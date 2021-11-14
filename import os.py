import os,sys
zhailu = open('zhailu1.file','w')
zhailu1 = open('zhailu.file','r')
sentence = []
sentence_searched = []
source = []
source_searched = []
theme = []
theme_searched = []
def Search():
    while True:
        keyword = input('请输入句子关键词：')
        if keyword == '':
            break
        for i in sentence:
            if keyword in i:
                sentence_searched.append(i)
                id = sentence.index(i)
                source_searched.append(source[id])
                theme_searched.append(theme[id])
        for u in sentence_searched:
            print('[句子]'+u)
            print('[出处]'+source_searched[sentence_searched.index(u)])
            print('[适用主题]'+theme_searched[sentence_searched.index(u)])
def ADD():
    while True:
        word_sentence = input('[句子]')
        if word_sentence == '':
            break
            print('[error]未填写必填项')
        else:
            sentence.append(word_sentence)
        word_source = input('[出处]')
        if word_source == '':
            source.append('')
        else:
            source.append(word_source)
        word_theme = input('[适用主题]')
        if word_theme == '':
            theme.append('')
        else:
            theme.append(word_theme)
        a = sentence.index(word_sentence)
        if source[a] == word_source and theme[a] == word_theme:
            print('已成功录入')
        else:
            print('[error]程序错误')
            os.system('pause')
            sys.exit()
# laoding
text = ''
d = zhailu1.read()
for i in d:
    if i != ",":
        text = text + i
    elif i == ',':
        if text == 'sentence':
            a = 1
            text = ''
        elif text == 'source':
            a = 2
            text = ''
        elif text == 'theme':
            a = 3
            text = ''
        if a == 1:
            sentence.append(text)
        elif a == 2:
            source.append(text)
        elif a == 3:
            theme.append(text)
for i in sentence:
    print(i)
# menu
event = input('[1]添加摘录\n[2]查询摘录\n[3]退出\n请选择:')
while True:
    if event == '1':
        ADD()
    elif event == '2':
        Search()
    elif event == '3':
        break