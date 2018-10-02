# -*- coding:utf-8 -*-

class Cat():
    """
    这是一个猫类
    这个和operation组成一个关于生命周期的问题
    """

    def __init__(self, name):
        print("初始化开始")
        self.name = name

    def eat(self):
        print("%s eat fish" % self.name)

    def drink(self):
        print("%s drink water" % self.name)

    def __del__(self):
        print("%s goodby" % self.name)


def operation(name):
    cat_one = Cat(name)
    cat_one.drink()
    print(cat_one.name)
    # del tom
    # print('-' * 30)


def createexcel(path):
    '''
    xlrd模块

    使用步骤及方法：

    打开文件：

    import xlrd

    excel=xlrd.open_workbook('E:/test.xlsx')



    获取sheet：

    table = excel.sheets()[0]       #通过索引获取

    table = excel.sheet_by_index(0)    #通过索引获取

    table = excel.sheet_by_name('Sheet1')   #通过表名获取



    备注：以下方法的操作都要在sheet基础上使用

    获取行数和列数：

    rows=table.nrows   #获取行数

    cols=table.ncols    #获取列数



    获取单元格值：

    Data=table.cell(row,col).value  #获取表格内容，是从第一行第一列是从0开始的，注意不要丢掉 .value



    获取整行或整列内容

    Row_values=table.row_values(i)   #获取整行内容

    Col_values=table.col_values(i)   #获取整列内容
    :param path:
    :return:
    '''
    import xlwt
    from xlrd import open_workbook
    from xlutils.copy import copy

    try:
        # 创建excel文件
        filename = xlwt.Workbook()
        # 给工作表命名，test
        sheet = filename.add_sheet("test")
        sheet._cell_overwrite_ok = True
        # 写入内容，第4行第3列写入‘张三丰’
        hello = u'张三丰'
        sheet.write(3, 2, hello)
        # 指定存储路径，如果当前路径存在同名文件，会覆盖掉同名文件
        filename.save("D:/test1.xls")
    except Exception, e:
        print(str(e))

    # 找到读取文件
    path = 'D:/test1.xls'
    # 打开excel文件
    date = xlrd.open_workbook(path)
    # 根据工作表名称，找到指定工作表  by_index(0)找到第N个工作表
    sheet = date.sheet_by_name('test')
    # 读取第四行第三列内容，cell_value读取单元格内容,指定编码
    value = sheet.cell_value(3, 2).encode('utf-8')
    print(value)

if __name__ == "__main__":
    # 生命周期问题
    # flag = 1
    # if flag:
    #     operation('tom')
    #     print 'test'
    # else:
    #     cat_one = Cat('tom')
    #     cat_one.drink()
    #     print(cat_one.name)
    #     # del tom
    #     # print('-' * 30)
    #     print 'test'

    # 读写excel
    from xlrd import open_workbook
    from xlutils.copy import copy

    print 'ssss'
    path = 'D:/test1.xls'
    rexcel = open_workbook(path)  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    print rows
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    values = ["1", "2", "3"]
    row = rows
    for value in values:
        table.write(row, 0, value)  # xlwt对象的写方法，参数分别是行、列、值
        table.write(row, 1, "haha")
        table.write(row, 2, "lala")
        row += 1
    excel.save(path)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel
