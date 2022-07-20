import sys


def loading():
    line = []
    text = ''
    zhailu = open('./zhailu.file', 'r')
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
        time = 0
        for c in line:
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
    zhailu.close()
    print('[system]文件加载成功')
    return line


def Search(the_list, keyword, theme, source, author):
    try:
        sentences = []
        themes = []
        sources = []
        authors = []
        time = 0
        for c in the_list:
            time = time + 1
            if time == 5 or time > 5:
                time = 1
            if time == 1:
                sentences.append(c)
            elif time == 2:
                themes.append(c)
            elif time == 3:
                sources.append(c)
            elif time == 4:
                authors.append(c)
        sentences_searched = []
        if keyword != '':
            for i in sentences:
                if keyword in i:
                    sentences_searched.append(i)
        #   elif theme != '':
        #        for i in themes:
        #            if keyword in i:
        #                sentences_searched.append(i)
        #    elif source != '':
        #        for i in sources:
        #            if keyword in i:
        #                sentences_searched.append(i)"
        id_ = 0
        print('已搜到与“' + keyword + '”相关摘录')
        for c in sentences_searched:
            print('[' + str(id_) + ']' + c)
            id_ = int(id_) + 1
        id = input('请选择：')
        id = sentences.index(sentences_searched[int(id)])
        print('[句子]' + sentences[id])
        if '《' in sources[id] and '》' in sources[id]:
            print('[出处]' + authors[id] + sources[id])
        else:
            print('[出处]' + authors[id] + '《' + sources[id] + '》')
        print('[适用主题]' + themes[id])
    except IndexError:
        if keyword == '':
            main('', True)
        else:
            print('找不到相关信息')
            main(2, True)
    except ValueError:
        if keyword == '':
            main('', True)
        else:
            print('找不到相关信息')
            main(2, True)


def save(the_list):
    zhailu = open('zhailu.file', 'w')
    sentences = []
    themes = []
    sources = []
    authors = []
    time = 0
    for i in the_list:
        time = time + 1
        if time == 5:
            time = 1
        if time == 1:
            sentences.append(i)
        elif time == 2:
            themes.append(i)
        elif time == 3:
            sources.append(i)
        elif time == 4:
            authors.append(i)
    for i in sentences:
        zhailu.write(i)
        zhailu.write('|' + themes[sentences.index(i)])
        zhailu.write('|' + sources[sentences.index(i)])
        zhailu.write('|' + authors[sentences.index(i)] + '\n')
    zhailu.close()


def main(choice, pass_run):
    global lists
    if choice == '':
        print('[system]请选择以下操作\n[1]添加摘录\n[2]搜索摘录\n[3]退出')
        choice = input('请选择：')
    if pass_run== False:
        source_last = ''
        author_last = ''
        try:
            lists = loading()
        except FileNotFoundError:
            zhailu = open('./zhailu.file', 'w')
            lists = loading()

    try:
        while True:
            if choice == '1':
                sentences = []
                themes = []
                sources = []
                authors = []
                time = 0
                for c in lists:
                    time = time + 1
                    if time == 5:
                        time = 1
                    if time == 1:
                        sentences.append(c)
                    elif time == 2:
                        themes.append(c)
                    elif time == 3:
                        sources.append(c)
                    elif time == 4:
                        authors.append(c)
                while True:
                    is_input = True
                    sentence = input('[句子]')
                    if sentence == '':
                        main('', True)
                    else:
                        for i in sentences:
                            if sentence == i:
                                print('[错误]句子重复')
                                is_input = False
                    if is_input == True:
                        theme = input('[主题]')
                        source = input('[出处]')
                        author = input('[作者]')
                        lists.append(sentence)
                        if theme == '':
                            lists.append('')
                        else:
                            lists.append(theme)
                        if source == ' ':
                            lists.append('')
                            source_last = ''
                        elif source == '':
                            lists.append(source_last)
                        else:
                            source_last = source
                            lists.append(source)
                        if author == '':
                            lists.append(author_last)
                        elif author == ' ':
                            lists.append('')
                            author_last = ''
                        else:
                            lists.append(author)
                            author_last = author
            elif choice == '2':
                keyword = input('关键词：')
                theme = input('适用主题：')
                source = input('出处：')
                author = input('作者：')
                Search(lists, keyword, theme, source, author)
            elif choice == '3':
                is_exit = input('是否退出[y/n] ')
                if is_exit == 'y':
                    save(lists)
                    sys.exit()
            else:
                print('请重新输入')
                main('', True)
    except KeyboardInterrupt:
        save(lists)
        print('已退出')
        sys.exit()
        input()


if __name__ == '__main__':
    main('', False)
