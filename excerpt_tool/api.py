from excerpt_tool.main import save
def write(sentence,theme,source,author,type_,mean):
    lists = []
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