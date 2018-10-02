#coding: utf-8

import os, traceback

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    '''
    输出目录下所有文件，不包括子目录的文件
    :param filepath: 文件夹
    :return:
    '''
    filepath = filepath.decode('utf8')
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        print child


# 读取文件内容并打印
def readFile(filename):
    '''
    读取文件内容
    :param filename:
    :return:
    '''
    filename = filename.decode('utf8')
    fopen = open(filename, 'r')  # r 代表read
    print "读取到得内容如下："
    for eachLine in fopen:
        print eachLine
    fopen.close()


# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
    '''
    写文件
    :param filename:
    :return:
    '''
    filename = filename.decode('utf8')
    fopen = open(filename, 'w')
    print "\r请任意输入多行文字", " ( 输入 .号回车保存)"
    while True:
        aLine = raw_input()
        if aLine != ".":
            fopen.write('%s%s' % (aLine, os.linesep))
        else:
            print "文件已保存!"
            break
    fopen.close()

#查找文件名中包含关键词的文件
def search_dir(s, path=os.path.abspath('.'),files = []):
    '''
    删除文件夹中特定文件名的文件
    os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    os.path.splitext(path)
    分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
    os.path.splitext('c:\\csv\\test.csv')
    ('c:\\csv\\test', '.csv')
    :param s:需要删除的文件名
    :param path:文件夹路径，默认为py文件所在文件夹
    :param files:删除的文件的集合（好像意义不大）
    :return:
    '''
    path = path.decode('utf8')
    try:
        for x in os.listdir(path):
            print x
            path_now = os.path.join(path, x)
            if os.path.isfile(path_now) and s == x: #in os.path.splitext(x)[0] 未注释的事匹配文件名+文件格式，注释后面是只匹配文件名
                #删除查找到的文件
                print 'find ......'+path_now
                # os.remove(path_now)
                if x not in files:
                    files.append(x)
            elif os.path.isdir(x):
                search_dir(s=s, path=os.path.join(path_now), files=files)
        print files
        return files
    except Exception, e:
        print traceback.format_exc()
        print e


def gci(filepath):
#遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            print os.path.join(filepath,fi_d)

if __name__ == "__main__":
    # # 在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转意
    # # 字符串加u表示将后面跟的字符串以unicode格式存储
    # pathfile = r'D:\测试'
    # #处理字符问题的最佳方法
    # # import chardet
    # # print chardet.detect(pathfile)
    # result = search_dir(s='xxx.ini', path=pathfile) #, path=pathfile

    # filePathC = "D:\\test"
    # eachFile(filePathC)
    #
    # filePath = "D:\\test\\xxx.ini"
    # readFile(filePath)

    # filePathI = "D:\\test\\xxx.ini"
    # writeFile(filePathI)

    pathfile = r'/Users/yefei/Downloads'
    # 这里没把编码变换放到函数内部，是因为gci里面有递归，会造成错误，必须使得所有传入的参数都是Unicode
    pathfile = pathfile.decode('utf8')
    gci(pathfile)
