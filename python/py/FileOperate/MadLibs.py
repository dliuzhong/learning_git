import os
def backAnOrA(word):
    Antext = ['A', 'E', 'I', 'O', 'F','H', 'L', 'M', 'N', 'R', 'S', 'X']
    if len(word) < 1:
        return 'a'
    if word[0] in Antext:
        return 'an'
    else:
        return 'a'

libsFile = open('/Users/liuyuanzhong/Documents/learning/python/py/FileOperate/libs.txt')
content = libsFile.read()
libsFile.close()
replace_text = ['ADJECTIVE', 'NOUN', 'VERB', 'NOUN']
for t in replace_text:
    print('Enter ' + backAnOrA(t) + ' ' + t.lower())
    content = content.replace(t, input(), 1)
print('After replace:')
print(content)
libsNewFile = open('/Users/liuyuanzhong/Documents/learning/python/py/FileOperate/libs_new.txt', 'w')
libsNewFile.write(content)
libsNewFile.close()
print('into libs_new.txt')
