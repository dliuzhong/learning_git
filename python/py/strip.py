#!python 3
# 写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。
# 如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
# 否则，函数第二个参数指定的字符将从该字符串中去除。

import re
def strip(str, str_replace):
    if str == None:
        return str
    if str_replace == None:
        str = re.sub(r'\A\s+', '', str)
        str = re.sub(r'\s+\A', '', str)
    else:
        str = re.compile(str_replace).sub("", str)
    return str

print(strip('   57854 ', '57'))