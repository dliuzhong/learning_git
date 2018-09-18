#!python3

# copyExtendsFile.py
# 遍历一个目录树，查找特定扩展名的文件(诸如.pdf 或.jpg)。

import os, re, shutil

def copyExtendsFiles(folder, extendsName, disSrcFolder):
    regExtendsFile = re.compile(r"""
        (.*?)
        (\."""+extendsName+""")$
    """, re.VERBOSE)
    absSrcPath = os.path.abspath(folder)
    disPath = os.path.abspath(disSrcFolder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            regGroup = regExtendsFile.search(filename)
            if regGroup == None:
                continue
            srcPath = os.path.join(absSrcPath, foldername, filename)
            print("Copy File: %s... from %s to folder %s " % (filename, srcPath, disPath))
            try:
                shutil.copy(srcPath, disPath)
                print("Done!")
            except:
                print("Skip!")
            
    print("All Done!")
        
        


copyExtendsFiles('.', 'zip', './disCopy')
