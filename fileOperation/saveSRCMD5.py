#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
该程序用计算&保存目录下所有文件的md5，格式为  md5 文件名 为一行 respath为需要计算md5的目录，
srcMd5Path是计算后md5保存的路径
'''

import os
import time
import md5
import sys
import socket
import subprocess
import shutil

# respath = r"C:\\Users\\feiye\\AppData\\Roaming\\Tencent\\HuaYang\\App"
# verpath = r"I:\\tx3_pre\\tx3\\update.ini"
# srcMd5Path = r"C:\\Users\\feiye\\Desktop\\"
# downloadMd5Path = r"I:\\tx3_pre\\checkMD5\\MD5download\\"
# programmer = "gzyefei@corp.netease.com"
# P2PUpdaterExe = "P2PUpdater.exe"
# filename = 'HuaYang_zeng.txt'

respath = r"/Users/yefei/Documents/Project/newstock/"
# verpath = r"I:\\tx3_pre\\tx3\\update.ini"
srcMd5Path = r"/Users/yefei/Documents/"  #注意一定要加最后的斜杆，要不然文件名就是documentshuayang_zeng
# downloadMd5Path = r"I:\\tx3_pre\\checkMD5\\MD5download\\"
programmer = "gzyefei@corp.netease.com"
# P2PUpdaterExe = "P2PUpdater.exe"
filename = 'HuaYang_zeng.txt'

# get md5 of a input string


def GetStringMD5(str):
    m = md5.new()
    m.update(str)
    return m.hexdigest()


# get md5 of a input file


def GetFileMD5(file):
    fileinfo = os.stat(file)
    if int(fileinfo.st_size)/(1024*1024)>1000:
        return GetBigFileMD5(file)
    m = md5.new()
    f = open(file,'rb')
    m.update(f.read())
    f.close()
    return m.hexdigest()


# get md5 of a input bigfile


def GetBigFileMD5(file):
    m = md5.new()
    f = open(file,'rb')
    maxbuf = 8192
    while 1:
        buf = f.read(maxbuf)
        if not buf:
            break
        m.update(buf)
    f.close()
    return m.hexdigest()


def getRelativePath(root,file):
    num = str(file).find(str(root))
    RelativePath = str(file)[num+len(str(root))+1:]
    return RelativePath
    # print 'RelativePath' + RelativePath


# get md5 of a input folder.
# result will be output to the specified file


def GetBetchFilesMD5(dir,outMD5File):
    print 'in GetBetchFilesMD5'
    result = {}
    print outMD5File
    outfile = open(outMD5File,'w')
    print dir
    for root ,subdirs, files in os.walk(dir):
        for file in files:
            # print file, getRelativePath(respath, root)
            if file in result.keys():
                print "repeat key"
                print file
            filefullpath = os.path.join(root, file)
            md5 = GetFileMD5(filefullpath)
            result[file] = md5

            # 第三个是相对的路径，因为有时候只考虑md5和文件名会有一个问题，那就是如果其他文件夹有一个同样的文件，
            # 那么在leftonly就会显示出来，因为刚开始碰到的时候他就删除了。加一个路径，可以避免这个问题
            text = md5 + "  " + file + "  " + getRelativePath(respath, root) + "\n"
            outfile.write(text)
            #print text
            #print filefullpath+'   md5:   '+md5+"\n"
    outfile.close()
    return True


def sendTo(result,name,sendType,filename):
    #print text
    text = 'left:src='+ filename + '\r\nright:mailDownload='+filename+'\r\n'
    for key,val in result.iteritems():
        text += key + '=['
        for item in val:
            text +=item+','
        text +=']'
    # popo({name:text},sendType)
    return "True"


def getName(filepath):
    fobj = open(filepath)
    for line in fobj.readlines():
        if "Version=" in line:
            filename = line.strip().split('Version=')[1].strip()
            fobj.close()
        return filename
    else:
        fobj.close()
    return None


def mailFile(path,filename):
    recepients = ["grp.tx3qc@corp.netease.com"]
    recepientsCC = []
    subject = "MD5src_" + filename
    message = 'test'
    if os.path.exists(path+filename):
        flag = mailto.sendMail(recepients,recepientsCC,subject, message, path+filename)
    return True


def checkProcess(PROCESSNAME):      
    NOW=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    command = 'tasklist'
    list1=os.popen(command).read().split('\n')
    for item in list1:
        pos=-1
        if PROCESSNAME in item:             
            log = str(NOW)+' : '+item+'\n'
            print log
            pos=1
            break
    if pos == -1:
        log = str(NOW)+' : No Process!\n' + str(PROCESSNAME)
        print log
        return False
    else:
        return True
    
if __name__ == "__main__":
    # now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    # filename1 = now +'.txt'
    print 'in main'
    # if os.path.exists(srcMd5Path+filename):
    #     print "src file exists. do not run.--",filename
    #     sys.exit()
    flag=GetBetchFilesMD5(respath,srcMd5Path+filename)
    
    if flag:  # flag == True
        print "send to",flag
        # popo({programmer:'saveSRCMD5:save md5file succeed'+filename},1)
