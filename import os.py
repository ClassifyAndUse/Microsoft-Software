import os
zhailu = open('zhailu1.file',w)
zhailu1 = open('zhailu.file',r)
sentence = []
sentence_searched = []
source = []
source_searched = []
theme = []
theme_searched = []
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
