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
    keyword = input('请输入句子关键词：')
    for i in sentence:
        if keyword in i:
            sentence_searched
def ADD():
    word_sentence = input('[句子]')
    if word_sentence == '':
        print('[error]未填写必填项')
    else:
        sentence.append(word_sentence)
    word_source = input('[来源]')
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
for i in zhailu1:
    if i != "|":
        text = text + i
    elif i == '|':
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
# menu
event = input('[1]添加摘录\n[2]查询摘录\n请选择:')
if event == '1':
    ADD()
elif event == '2':
    pass