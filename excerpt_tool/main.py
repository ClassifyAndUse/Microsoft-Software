# encoding=’gb2312’
import sys
import os


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
    try:
        log = open('./sentence_log', 'r')
        for i in log:
            Value = i + Value
            print(Value)
    except FileNotFoundError:
        print('找不到旧文件')
        main('', False)
        log = open('./sentence_log', 'w')
        log.write(len(sentence))
    print('[system]文件加载成功')
    return line


def translate():
    line = []
    text = ''
    try:
        zhailu = open('./zhailu.file', 'r')
    except FileNotFoundError:
        print('找不到旧文件')
        main('', False)
        zhailu = open('./zhailu.file', 'w')
    for i in zhailu:
        for a in i:
            if a == '\n' or a == '|' or a == '':
                line.append(text)
                text = ''
            else:
                text = text + a
    zhailu.close()
    print('[system]旧文件加载成功')
    sentences = []
    themes = []
    sources = []
    authors = []
    types = []
    means = []
    time = 0
    for c in line:
        time = time + 1
        if time == 5:
            time = 1
        if time == 1:
            sentenc = c
            sentences.append(c)
        elif time == 2:
            themes.append(c)
        elif time == 3:
            sources.append(c)
        elif time == 4:
            authors.append(c)
            if len(sentenc) > 10:
                types.append('句子')
            else:
                print('你认为 ' + sentenc + ' 是什么类型')
                while True:
                    print('[system]请选择以下类型\n[1]词语\n[2]句子')
                    type_ = input('[类型]')
                    if type_ == '':
                        print('[system]错误！该项不得为空')
                    elif type_ == '1':
                        types.append('词语')
                        break
                    elif type_ == '2':
                        types.append('句子')
                        break
                    else:
                        print('[system]错误！没有这个选项')
            means.append(' ')
    line = []
    for i in sentences:
        id_ = sentences.index(i)
        line.append(i)
        line.append(themes[id_])
        line.append(sources[id_])
        line.append(authors[id_])
        line.append(types[id_])
        line.append(means[id_])
    save(line)
    main('', False)


def Search(the_list, keyword, theme, source, author, type_):
    try:
        sentences = []
        themes = []
        sources = []
        authors = []
        types = []
        means = []
        time = 0
        for c in the_list:
            time = time + 1
            if time == 7:
                time = 1
            if time == 1:
                sentences.append(c)
            elif time == 2:
                themes.append(c)
            elif time == 3:
                sources.append(c)
            elif time == 4:
                authors.append(c)
            elif time == 5:
                types.append(c)
            elif time == 6:
                means.append(c)
        sentences_searched = []
        if keyword != '':
            for i in sentences:
                if keyword in i:
                    sentences_searched.append(i)
        elif keyword == '':
            for i in sentences:
                sentences_searched.append(i)
        if theme != '':
            for i in sentences_searched:
                id_ = sentences.index(i)
                if theme != themes[id_]:
                    sentences_searched.remove(sentences_searched[sentences_searched.index(i)])
        if source != '':
            for i in sentences_searched:
                id_ = sentences.index(i)
                if source != sources[id_]:
                    sentences_searched.remove(sentences_searched[sentences_searched.index(i)])
        if type_ != '':
            for i in sentences_searched:
                id_ = sentences.index(i)
                if type_ != types[id_]:
                    sentences_searched.remove(sentences_searched[sentences_searched.index(i)])
        if author != '':
            for i in sentences_searched:
                id_ = sentences.index(i)
                if author != authors[id_]:
                    sentences_searched.remove(sentences_searched[sentences_searched.index(i)])
        id_ = 0
        print('已搜到与“' + keyword + '”相关摘录')
        for c in sentences_searched:
            print('[' + str(id_) + ']' + c)
            id_ = int(id_) + 1
        id_ = input('请选择：')
        id_ = sentences.index(sentences_searched[int(id_)])
        print('[句子]' + sentences[id_])
        if '《' in sources[id_] and '》' in sources[id_]:
            print('[出处]' + authors[id_] + sources[id_])
        else:
            print('[出处]' + authors[id_] + '《' + sources[id_] + '》')
        if means[id_] != '':
            print('[意思]' + means[id_])
        print('[适用主题]' + themes[id_])
    except IndexError:
        if keyword == '':
            main('', True)
        else:
            print('找不到相关信息')
            main('2', True)
    except ValueError:
        if keyword == '':
            main('', True)
        else:
            print('找不到相关信息')
            main('2', True)


def save(the_list):
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


def main(choice, pass_run):
    global lists
    if choice == '':
        print('[system]请选择以下操作\n[1]添加摘录\n[2]搜索摘录\n[3]转换\n[4]我的进步\n[5]退出')
        choice = input('请选择：')
    if pass_run == False:
        source_last = ''
        author_last = ''
        try:
            lists = loading()
        except FileNotFoundError:
            zhailu = open('./zhailu.cau', 'w')
            zhailu.close()
            lists = loading()
    try:
        while True:
                sentences = []
                themes = []
                sources = []
                authors = []
                types = []
                means = []
                time = 0
                for c in lists:
                    time = time + 1
                    if time == 7:
                        time = 1
                    if time == 1:
                        sentences.append(c)
                    elif time == 2:
                        themes.append(c)
                    elif time == 3:
                        sources.append(c)
                    elif time == 4:
                        authors.append(c)
                    elif time == 5:
                        types.append(c)
                    elif time == 6:
                        means.append(c)
        if choice == '1':
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
                    if len(sentence) > 10:
                        type_ = '句子'
                    else:
                        while True:
                            print('[system]请选择以下类型\n[1]词语\n[2]句子')
                            type_ = input('[类型]')
                            if type_ == '':
                                print('[system]错误！该项不得为空')
                            elif type_ == '1':
                                type_ = '词语'
                                break
                            elif type_ == '2':
                                type_ = '句子'
                                break
                            else:
                                print('[system]错误！没有这个选项')
                    author = input('[作者]')
                    mean = input('[意思]')
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
                    lists.append(type_)
                    if mean != '':
                        lists.append(str(mean))  # 意思
                    else:
                        lists.append(' ')
                    save(lists)
        elif choice == '2':
            keyword = input('关键词：')
            theme = input('适用主题：')
            source = input('出处：')
            author = input('作者：')
            type_ = input('类型：')
            Search(lists, keyword, theme, source, author, type_)
        elif choice == '3':
            translate()
        elif choice == '5':
            is_exit = input('是否退出[y/n] ')
            if is_exit == 'y':
                save(lists)
                sys.exit()
        elif choice == '4':
                len(sentences)
        else:
                print('请重新输入')
                main('', True)
    except KeyboardInterrupt:
        save(lists)
        c =open('./sentence_log', 'w')
        c.write(len(sentences))
        print('已退出')
        sys.exit()
        input()


if __name__ == '__main__':
    main('', False)
