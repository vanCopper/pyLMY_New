#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/6/21'
import time
day_of_week={
    '1':'一',
    '2':'二',
    '3':'三',
    '4':'四',
    '5':'五',
    '6':'六',
    '7':'日'
}
def getTime():
    dt = {}
    dt['curTime'] = time.strftime("%H:%M")
    # print(time.strftime("%w"), time.strftime("%d"), time.strftime("%m"))
    dt['date'] = '{}月{}日 星期{}'.format(time.strftime('%m').replace('0',''), time.strftime('%d').replace('0',''), day_of_week[time.strftime('%w')])
    # print('05'.replace('0',''))
    # print('11'.replace('0',''))
    return dt
