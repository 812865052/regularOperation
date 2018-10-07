#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
该程序用来对比两个不同的文件之间的md5和文件名是否一致，最后列出各个文件中不同的文件
两个txt文件每行都是文件名+md5，文件名相同并且md5也相同才行。列出两个文件中不同的
'''

import os
dirLeft = "C:\\Users\\feiye\\Desktop\\HuaYang.txt"
dirRight = "C:\\Users\\feiye\\Desktop\\HuaYang_zeng.txt"
unUse = 'C:\\Users\\feiye\\Desktop\\unUse.txt'


def fileName(dir):
    leftOnly = []
    I=os.listdir(dir)
    for targetFile in I:
        # targetFile=os.path.join(dir,targetFile) #os.path.isfile和os.path.isdir区分是文件还是目录
        targetFile = targetFile[:-4]
        leftOnly.append(targetFile)
        # print targetFile
        # print os.path.isfile(targetFile)
        # print targetFile.find('tx-')
        # print targetFile[18:21]
        # if os.path.isfile(targetFile) and targetFile[18:21]=='tx-':
        #     os.remove(targetFile)
    return leftOnly


def readFile(dir):
    rightOnly = []
    fobj = open(dir,'rb')
    for line in fobj.readlines():
        # print line
        if line.strip() == '':
            continue
        # print line
        rightOnly.append(line)
    # print rightOnly
    return rightOnly


def diff(left, right):
    result = {'left_only':[],'right_only':[]} 
    # print result
    leftOnly = []
    rightOnly = []
    left_num = 0
    for key in right:
        # if key in right:
        #     continue
        if key not in rightOnly:   # 防止加入了重复的key，这样后面删除的时候会出bug
            rightOnly.append(key)
    for key in left:
        if key not in rightOnly:  # 这里要判断是否在rightOnly里面，而不是right里面
            # print 'not same:',key
            # sys.exit()
            # if key in leftOnly:
            #     continue
            leftOnly.append(key)  # left才有的
            left_num = left_num+1
        else:
            rightOnly.remove(key)  # right才有的
    result['left_only'] = leftOnly
    result['right_only'] = rightOnly
    # print left_num
    # print result
    return result


def writeFile(src):
    # print src.keys()
    file_object = open(unUse, 'w')
    file_object.write('right_only=增量升级 left_only=正常花样\n') #'\r\n'
    file_object.write('md5 文件名 相对路径\n')
    for key in src.keys():
        # print key
        innerSrc = src[key]
        print innerSrc
        num = 0
        file_object.write(key+'\r')
        for line in innerSrc:
            # print line
            file_object.writelines(line) # file_object.write(line)
            num = num + 1
        file_object.write(str(num)+'\r')
    file_object.close()


if __name__ == "__main__":
    # left = fileName(dirSrc)
    # print type(left)
    right = readFile(dirRight)
    left = readFile(dirLeft)
    result = diff(left, right)
    # print result['left_only']
    # print result['right_only']
    print result
    writeFile(result)