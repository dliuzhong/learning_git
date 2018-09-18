#!python 3
# 扩展本章中的多重剪贴板程序，
# 增加一个 delete <keyword>命令行参数，
# 它将 从 shelf 中删除一个关键字。
# 然后添加一个 delete 命令行参数，它将删除所有关键字。

import sys, shelve, pprint

def deleteAllShelve():
    shelveFile =  shelve.open('mydata')
    data = []
    shelveFile['data'] = data
    print(pprint.pformat(shelveFile['data']))
    print('Deleted All.')
    shelveFile.close()

def deleteShelve(keyword):
    shelveFile = shelve.open('mydata')
    data = shelveFile['data']
    if keyword not in data:
        print('Warning: ' + keyword + ' not exist.')
    else:
        del data[data.index(keyword)]
        shelveFile['data'] = data
        print(pprint.pformat(shelveFile['data']))
    shelveFile.close()

def addShelve(keyword):
    shelveFile = shelve.open('mydata')
    data = shelveFile['data']
    if keyword in data:
        print('Warning: ' + keyword + ' exist.')
    else:
        data += [keyword]
        shelveFile['data'] = data
        print(pprint.pformat(shelveFile['data']))
    shelveFile.close()

if len(sys.argv) == 2:
    if sys.argv[1] == 'delete':
        deleteAllShelve()
    else:
        print('Usage: py3 shelve.argv.py delete -- delete data in shelve')
        sys.exit()
elif len(sys.argv) == 3:
    keyword = sys.argv[2]
    if sys.argv[1] == 'delete':
        deleteShelve(keyword)
    elif sys.argv[1] == 'add':
        addShelve(keyword)
    else:
        print('Usage: py3 shelve.argv.py add/delete [keyword] -- add/delete data in shelve')
        sys.exit()
else:
    print('Usage: py3 shelve.argv.py add/delete [keyword] -- add/delete data in shelve')
    sys.exit()
