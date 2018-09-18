#!python 3
# 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
# 强口令的 定义是:长度不少于 8 个字符，同时包含大写和小写字符，
# 至少有一位数字。你可能需要用多个正则表达式来测试该字符串，
# 以保证它的强度。
import sys, re
def checkValidPassword(str):
    # length >= 8, include Uper, lower alphabet
    if len(str) < 8:
        return False
    if re.compile(r'[a-z]+').search(str) == None:
        return False
    if re.compile(r'[A-Z]+').search(str) == None:
        return False
    if re.compile(r'\d+').search(str) == None:
        return False
    return True
if len(sys.argv) < 2:
    print('Usage: py checkPassword.py [password] - check your password valid')
    sys.exit()
pwStr = sys.argv[1]
if checkValidPassword(pwStr): 
    print('Valid')
else:
    print('Unvalid')