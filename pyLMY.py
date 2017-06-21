# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyLMY.py'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import LMY
import DateUtil
import weatherUtil

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 时间更新
def updateTime():
    dt = DateUtil.getTime()
    ui.timeLabel.setText(dt.get('curTime'))
    ui.dateLabel.setText(dt.get('date'))

# 更新天气
def updateWeather():
    # {'text': '多云', 'code': '4', 'temperature': '25'}
    nowObj = weatherUtil.getNowWeather()
    ui.nowText.setText(nowObj.get('text'))
    ui.nowTmp.setText(nowObj.get('temperature')+'°C')
    ui.nowIcon.setPixmap(QtGui.QPixmap('images/'+nowObj.get('code')+'.png'))
    # [{'date': '2017-06-21', 'text_day': '阵雨', 'code_day': '10', 'text_night': '阴', 'code_night': '9', 'high': '26', 'low': '23', 'precip': '', 'wind_direction': '东南', 'wind_direction_degree': '135', 'wind_speed': '10', 'wind_scale': '2'}, {'date': '2017-06-22', 'text_day': '阵雨', 'code_day': '10', 'text_night': '阴', 'code_night': '9', 'high': '27', 'low': '23', 'precip': '', 'wind_direction': '东', 'wind_direction_degree': '90', 'wind_speed': '10', 'wind_scale': '2'}, {'date': '2017-06-23', 'text_day': '中雨', 'code_day': '14', 'text_night': '暴雨', 'code_night': '16', 'high': '27', 'low': '23', 'precip': '', 'wind_direction': '东', 'wind_direction_degree': '90', 'wind_speed': '15', 'wind_scale': '3'}]
    dailyObj = weatherUtil.getDaysWeather()
    # 今日
    ui.day1Text.setText(dailyObj[0]['text_day'])
    ui.day1Tmp.setText(dailyObj[0]['low']+'°/'+dailyObj[0]['high']+'°')
    ui.day1Icon.setPixmap(QtGui.QPixmap('images/'+dailyObj[0]['code_day']+'.png'))
    # 第二天
    ui.day2Text.setText(dailyObj[1]['text_day'])
    ui.day2Tmp.setText(dailyObj[1]['low']+'°/'+dailyObj[1]['high']+'°')
    ui.day2Icon.setPixmap(QtGui.QPixmap('images/'+dailyObj[1]['code_day']+'.png'))
    # 第三天
    ui.day3Text.setText(dailyObj[2]['text_day'])
    ui.day3Tmp.setText(dailyObj[2]['low']+'°/'+dailyObj[2]['high']+'°')
    ui.day3Icon.setPixmap(QtGui.QPixmap('images/'+dailyObj[2]['code_day']+'.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = LMY.Ui_LYM()
    ui.setupUi(MainWindow)

    if os.uname()[0]=="Linux":
        MainWindow.showFullScreen()
    else:
        MainWindow.showNormal()

    updateTime()
    updateWeather()
    timer = QTimer()
    timer.timeout.connect(updateTime)
    timer.start(5000)#时间更新 一分钟
    sys.exit(app.exec_())

