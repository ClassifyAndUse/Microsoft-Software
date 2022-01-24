import os,sys
def laoding():
    line = []
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
def Search(the_list,keyword,theme,source,author):
    sentence = []
    theme = []
    source = []
    author = []
    time = 0
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
def add(sentences,themes,sources,authors):
    while True:
        is_input = True
        sentence = input('[句子]')
        for i in sentences:
            if sentence == i:
                print('[错误]句子重复')
                is_input = False
                break
        theme = input('[主题]')
        source = input('[出处]')
        author = input('[作者]')
        if is_input == True:
            sentences.append(sentence)
            themes.append(theme)
            sources.append(source)
            authors.append(author)
def save(sentences,themes,sources,authors):
    zhailu1 = open('zhailu1.file','w')
    for i in sentences:
        zhailu1.write(i)
        zhailu1.write('|'+themes[sentences.index(i)])
        zhailu1.write('|'+sources[sentences.index(i)])
        zhailu1.write('|'+authors[sentences.index(i)]+'\n')
    zhailu1.close()
    os.rename('zhailu1.file','zhailu.file')
        