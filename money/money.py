#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
该程序用计算年化收益，base表示本金，rate表示年化利率，day表示投资天数
'''

from decimal import Decimal
import time
import datetime
from datetime import date

def money(base, rate, day):
    temp = base*rate*day/365
    #i = Decimal(money(base, rate, day).quantize(Decimal('0.00')))
    print u'收益为 ' + format(temp, '0.2f')
    return temp


def year_rate(income, base, day):
    temp = base*day/(income*365)
    print u'年化为 ' + format(temp, '0.2f')
    return temp

def insertdate(year,month,day,data,companylist):
    while (datetime.date.today() > date(year, month, day)):
        dict = {}
        month = month + 1
        if month > 12:
            year = year + 1
            month = 1
        if (datetime.date.today() > date(year, month, day)):
            dict['date'] = date(year, month, day)
            dict[companylist[0]] = 0
            dict[companylist[1]] = 0
            dict[companylist[2]] = 0
            data.append(dict)
    print data
    return data

def insertcompany(data,table,company):
    for i in data:
        if date(2017,4,8) == i['date']:
            print i
    return 0


if __name__ == '__main__':
    # year_rate(1.5, 8100, 1)
    # money(8089, 0.07, 1)

    # print time.strptime('2008-02-14', '%Y-%m-%d')
    # struct_time = time.strptime("30 Nov 17", "%d %b %y")
    # print time.strftime('%Y-%m-%d', struct_time)
    year = 2017
    month = 3
    day = 8
    data = []
    companylist = ['momo', 'baba', 'tencent']
    insertdate(year, month, day, data,companylist)


