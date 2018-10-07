#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
该程序用汇率优惠度
'''

from decimal import Decimal


def us(money, us_rate):
    temp = (money/us_rate)*100
    print u'银行兑换的美元为' + format(temp, '0.2f')
    return temp


def hk(money, hk_rate):
    temp = (money / hk_rate) * 100
    print u'银行兑换的港币为' + format(temp, '0.2f')
    return temp


def futu(us_money, futu_rate):
    temp = us_money*futu_rate
    print u'富途转换后的港币为' + format(temp, '0.2f')
    return temp


def choose(bank_money, futu_money):
    if(bank_money >= futu_money):
        print u'银行兑换港币为' + format(bank_money, '0.2f') + u' 富途兑换港币为' + format(futu_money, '0.2f')
        print u'银行兑换比富途兑换多' + format(bank_money - futu_money, '0.2f')
        print u'银行换港币更划算 直接兑换港币然后汇香港'
    else:
        print u'银行兑换港币为' + format(bank_money, '0.2f') + u' 富途兑换港币为' + format(futu_money, '0.2f')
        print u'富途兑换比银行兑换多' + format(futu_money - bank_money, '0.2f')
        print u'银行换美元更划算 兑换美元然后去富途换港币'


if __name__ == '__main__':
    money = 400000
    hk_rate = 85.26
    us_rate = 667.28
    futu_rate = 7.8065
    choose(hk(money, hk_rate), futu(us(money, us_rate), futu_rate))