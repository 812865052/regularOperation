#coding: utf-8

import os,string

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
            print (id)
            id = id + 1
            temp = id
            print ((int(temp / 10)))
            num = 0
            numstr = ''
            while temp != 0:
                temp = int(temp / 10)
                num = num + 1

            print (num)

            if num == 1:
                numstr = '000'+str(id)
            elif num == 2:
                numstr = '00'+str(id)
            elif num == 3:
                numstr = '0'+str(id)
            elif num == 4:
                numstr = str(id)

            wopen.write('%s' % eachLine)
            wopen.writelines('                     /protein_id="%s"' % numstr)
            wopen.write('\n')
        else:
            wopen.write('%s' % eachLine)
    print (id)
    ropen.close()
    wopen.close()


if __name__ == "__main__":
    filenameread = '/Users/yefei/Downloads/SA4769.prokka.gbk'
    filenamewrite = '/Users/yefei/Downloads/new_SA4769.prokka.gbk'
    TransFile(filenameread,filenamewrite)