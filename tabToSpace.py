# -*- coding: utf-8 -*-
"""
author:Robin Chan in lab313
usage: tab2space
a python script use to change tab to spaces
opts:
1--inputfilename
2--outputfilename
3--1/2 tab2space or space2tab
4--tabsize,means 1 tab = tabsize spaces
"""
# import getopt
import sys


def tab2spacefuc(inputfile, outputfile, tabsize):
    try:
        fp = open(inputfile, "r+")
        newfp = open(outputfile, "w")
    except Exception, info:
        print info
    inStr = '\t'
    outStr = tabsize * ' '
    for eachline in fp.readlines():
        newStr = eachline.replace(inStr, outStr)
        newfp.write(newStr)
    fp.close()
    newfp.close()


def space2tabfuc(inputfile, outputfile, tabsize):
    try:
        fp = open(inputfile, "r+")
        newfp = open(outputfile, "w")
    except Exception, info:
        print info
    # inStr = tabsize*' '
    # outStr = '\t'
    newStr = ''
    num = 0
    for eachline in fp.readlines():
        i = 0
        while i < len(eachline) - 1:
            i = i + 1
            if eachline[i] == ' ':
                num = num + 1
                if num == tabsize:
                    # eachline[i - tabsize:i] = '\t'
                    newStr = newStr + '\t'
                    newStr = newStr +eachline[i:]
            else:
                num = 0
                newStr = eachline
        newfp.write(newStr)
    fp.close()
    newfp.close()


if __name__ == "__main__":
    # inputfile = sys.argv[1]  # input file name
    # outputfile = sys.argv[2]
    inputfile = r'/Users/yefei/Downloads/tabToSpace.py'  # input file name
    outputfile = r'/Users/yefei/Downloads/tabToSpacesss.py'  # output file name
    if len(sys.argv[1:]) < 3:  # default set
        fuc = 2  # tab2space
        tabsize = 4  # default tabsize = 4,means 1 tab = 4 spaces
    else:
        fuc = sys.argv[3]  # tab2space or space2tab
        tabsize = sys.argv[4]  # tabsize
    if fuc == 1:
        tab2spacefuc(inputfile, outputfile, tabsize)
    else:
        space2tabfuc(inputfile, outputfile, tabsize)
