#coding: utf-8

import os

# 读取文件内容并打印
def TransFile(filenameread,filenamewrite):
    '''
    读取文件内容
    :param filename:
    :return:
    '''
    id = 0
    #python 2.7
    # readname = filenameread.decode('utf8')
    # ropen = open(readname, 'r')  # r 代表read
    # writename = filenamewrite.decode('utf8')
    # wopen = open(writename, 'w')  # r 代表read

    #python 3.0+
    ropen = open(filenameread, 'r')  # r 代表read
    wopen = open(filenamewrite, 'w')  # r 代表read
    for eachLine in ropen:
        if '/product="' in eachLine:
            # print eachLine
            id = id + 1
            wopen.write('%s' % eachLine)
            wopen.writelines('                     /protein_id="%d"' % id)
            wopen.write('\n')
        else:
            wopen.write('%s' % eachLine)
    print (id)
    ropen.close()
    wopen.close()


if __name__ == "__main__":
    filenameread = '/Users/yefei/Downloads/SA9628.gbff.gbk'
    filenamewrite = '/Users/yefei/Downloads/new_SA9628.gbff.gbk'
    TransFile(filenameread,filenamewrite)