# -*- coding:utf8 -*-
import xlwt
import xlrd


def wirte_excel(list_host_uid, list_uid, list_column, list_roomid, save_file):
    """写excel函数

    把list_host_uid, list_uid, list_column, list_roomid值依次填到一行excel中
    save_file是要保存的文件
    """
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet', cell_overwrite_ok=True)
    j = 0
    for column in list_column:
        worksheet.write(0, j, column)
        j = j + 1
    price = 2
    uid_length = len(list_uid)
    i = 0
    while(i < uid_length-1):
        worksheet.write(i+1, 0, list_uid[i])
        worksheet.write(i+1, 1, list_uid[i+1])
        worksheet.write(i+1, 2, price)
        worksheet.write(i+1, 3, list_roomid[i%14])
        worksheet.write(i+1, 4, list_host_uid[i%103])
        price = price + 2
        i = i + 1

    host_uid_length = len(list_host_uid)
    price = 2
    temp = 0
    while(temp < host_uid_length):
        worksheet.write(i, 0, list_uid[temp])
        worksheet.write(i, 1, list_host_uid[temp])
        worksheet.write(i, 2, price)
        worksheet.write(i, 3, list_roomid[temp%14])
        worksheet.write(i, 4, list_host_uid[temp])
        price = price + 2
        i = i + 1
        temp = temp + 1
        
    workbook.save(save_file)


def write_excel_2():
    file = xlwt.Workbook()
    table = file.add_sheet('sheet name')
    table.write(0,0,'test')
    #table = file.add_sheet('sheet name',cell_overwrite_ok=True)
    file.save('demo.xls')


def writeFile(save_file, txtFile):
    """读excel表，并把它以txt形式存下来

    save_file, txtFile分别表示excel文件和txt文件
    """
    data = xlrd.open_workbook(save_file)
    table = data.sheets()[0]
    nrows = table.nrows
    file_object = open(txtFile,'w')
    i = 0
    # \r 是回车，return
    # \n 是换行，newline
    while(i < nrows):
        for j in table.row_values(i):
            file_object.write(str(j)[0:-2]+' ')
        file_object.write('\n')
        i = i + 1
    # print table.row_values(2)
    # for j in table.row_values(2):
    #     print str(j)[0:-2]
    file_object.close()


def readFile(filename):
    """从txt文件中读取值并以list形式返回

    filename表示txt文件
    返回值形式为list
    """
    listNumber = []
    fobj = open(filename,'rb')
    for line in fobj.readlines():
        #print line
        if line.strip() == '':
            continue
        #print line
        listNumber.append(line)
    fobj.close()
    return listNumber


if __name__ == '__main__':
    """函数的目的就是从txt文件中读取值，然后以一定形式保存在excel中，然后读取excel内容，按行保存到txt文件中
    """
    # host_uid = "C:\\Users\\feiye\\Desktop\\list_host_uid.txt"
    # uid = "C:\\Users\\feiye\\Desktop\\list_uid.txt"
    # txtFile = "C:\\Users\\feiye\\Desktop\\uid.txt"
    # list_host_uid = readFile(host_uid)
    # list_uid = readFile(uid)
    # save_file = "C:\\Users\\feiye\\Desktop\\uid.xls"
    # list_column = ['uid', 'to_uid', 'price', 'room_id', 'host_uid']
    # list_roomid = [900160, 900161, 900162, 900163, 900164, 900165, 900150, 900151, 900152, 900153, 900154, 900156, 900157, 900159]
    # wirte_excel(list_host_uid, list_uid, list_column, list_roomid, save_file)
    # writeFile(save_file, txtFile)
    print 'a'+'\r'+'b'
    print 'c'+'\n'+'d'
    print 'e'+'\n\r'+'f'
    print 'g'+'\r\n'+'h'
    
