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
    print('[system]文件加载成功')
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
        print('added')
    zhailu.close()