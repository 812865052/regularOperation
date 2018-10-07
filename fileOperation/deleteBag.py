#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
dirSrc = "I:\\Netease\\tx3\\res\\universes\\eg\\"
dirObj = "C:\\Users\\gzyefei\\Desktop\\unUse.txt"

def deleteFile(dir,src):
	leftOnly = []
	I=os.listdir(dir)
	for targetFile in I:
		targetFilePath=os.path.join(dir,targetFile) #os.path.isfile和os.path.isdir区分是文件还是目录
		if os.path.isfile(targetFilePath) and targetFile in src: 
			os.remove(targetFile)
	return leftOnly

def readFile(dir):
	rightOnly = []
	fobj = open(dir,'rb')
	line = ''
	for line in fobj.readlines():
		#print line
		if line.strip() == '':
			continue
		try:
			words = line.strip().split('\\')
			key = words[1].strip()
			md5 = words[0].strip()
			line = words[2].strip()
			print key
		except:
			if not line.strip().split('/'):
				print line
			
				
			
		#print line
		line = line[:-3]
		rightOnly.append(line)
	return rightOnly

if __name__ == "__main__":
	src = readFile(dirObj)
	print '..........'
	print src
	print 'zhongyuan' in src
	deleteFile(dirSrc, src)