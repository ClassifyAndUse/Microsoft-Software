import os
zhailu = open('zhailu1.file',w)
zhailu1 = open('zhailu.file',r)
sentence = []
sentence_searched = []
source = []
source_searched = []
theme = []
theme_searched = []
for i in zhailu1:
    if i != "|":
        text = text + i
    elif i == '|'