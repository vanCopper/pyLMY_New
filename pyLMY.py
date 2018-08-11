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
import mailUtil
import time

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

say_hi={
        1 :u"早上好,Miya~",
        2 :u"午安,眯一会吧~",
        3 :u"下午也许比较忙,记得劳逸结合~",
        4 :u"马上就要下班啦~~~~(不加班的话)",
    }
# 时间更新
def updateTime():
    dt = DateUtil.getTime()
    ui.timeLabel.setText(dt.get('curTime'))
    ui.dateLabel.setText(dt.get('date'))
    global drink_visible
    global drink_stamp
    global gym_visible
    global gym_stamp

    if drink_visible is True:
        t_time = time.time() - drink_stamp
        if t_time > 60:
            drink_visible = False
            ui.widget_2.setVisible(False)
            ui.drinkButton.setVisible(False)
        else:
            drink_stamp = time.time();

    if gym_visible is True:
        t_time = time.time() - gym_stamp
        if t_time > 60:
            gym_visible = False
            ui.widget_2.setVisible(False)
            ui.gymButton.setVisible(False)
        else:
            gym_stamp = time.time()
    hour = int(dt.get('curHour'))
    global say_hi
    if hour > 17 and hour < 24:
        ui.helloMiya.setText(say_hi[4])
    elif hour >= 12 and hour <= 13:
        ui.helloMiya.setText(say_hi[2])
    elif hour > 9 and hour < 12:
        ui.helloMiya.setText(say_hi[1])
    elif hour > 13 and hour < 17:
        ui.helloMiya.setText(say_hi[3])

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
mails = []
def updateMail():
    newMails =  mailUtil.getMail()
    for n in newMails:
        mails.append(n)
    # ui.mailBrowser.setText(mails[0])
    # del mails[0]
    if len(mails) > 0 and ui.mailBrowser.isVisible() == False:
        ui.mailButton.setVisible(True)

drink_stamp = 0 # 提醒时的时间戳
drink_visible = False # 是否已经显示提醒
def updateDrink():
    ui.widget.setVisible(False)
    ui.widget_2.setVisible(True)
    ui.drinkButton.setVisible(True)
    ui.gymButton.setVisible(False)
    global drink_visible
    global drink_stamp
    drink_visible = True
    drink_stamp = time.time()

gym_stamp = 0 # 提醒时的时间戳
gym_visible = False # 是否已经显示提醒
def updateGym():
    ui.widget.setVisible(False)
    ui.widget_2.setVisible(True)
    ui.gymButton.setVisible(True)
    ui.drinkButton.setVisible(False)
    global gym_stamp
    global gym_visible
    gym_stamp = time.time()
    gym_visible = True

def readMail():
    print('readMail>>>>>')
    ui.mailButton.setVisible(False)
    ui.mailBrowser.setVisible(True)
    ui.closeMail.setVisible(True)
    ui.mailBrowser.setText(mails[0])
    del mails[0]

def closeMail():
    ui.mailBrowser.setVisible(False)
    ui.closeMail.setVisible(False)
    ui.mailBrowser.setText('')
# def startAni(display):
    # aniTimer = QTimeLine
if __name__ == '__main__':
    # print( time.strftime("%H"))
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = LMY.Ui_LYM()
    ui.setupUi(MainWindow)
    # ui.mailButton.setVisible(False)
    # ui.mailBrowser.setVisible(False)
    # ui.closeMail.setVisible(False)

    if os.uname()[0]=="Linux":
        MainWindow.showFullScreen()
    else:
        MainWindow.showNormal()

    # picon = QtGui.QPixmap('images/letter.png')
    # ui.mailButton.clicked.connect(readMail)
    # ui.closeMail.clicked.connect(closeMail)
    # ui.closeMail.setStyleSheet("QPushButton{background-color:transparent}")
    # ui.mailButton.setStyleSheet("QPushButton{background-color:transparent}")
    # ui.widget.setStyleSheet("background-color:#313339;")

    # ui.widget_2.setStyleSheet("background-color:#313339;")
    # ui.drinkButton.setStyleSheet("QPushButton{background-color:transparent}")
    # ui.gymButton.setStyleSheet("QPushButton{background-color:transparent}")
    # ui.widget_2.setVisible(False)
    # ui.widget.setVisible(False)
    # updateTime()
    updateWeather()
    # updateMail()

    timer = QTimer()
    timer.timeout.connect(updateTime)
    timer.start(5000)#时间更新 五秒刷新一次

    wtimer = QTimer()
    wtimer.timeout.connect(updateWeather)
    wtimer.start(1000*60*30)#天气更新 半小时刷新一次

    # mtimer = QTimer()
    # mtimer.timeout.connect(updateMail)
    # mtimer.start(1000*60*10)#读取邮件 十分钟一次
    # mtimer.start(1000*20)

    # drink_timer = QTimer()
    # drink_timer.timeout.connect(updateDrink)
    # drink_timer.start(1000*60*90)# 提醒喝水 一个半小时一次
    # drink_timer.start(1000*10) # 测试

    # gym_timer = QTimer()
    # gym_timer.timeout.connect(updateGym)
    # gym_timer.start(1000*60*120) # 提醒运动 两个小时一次
    # gym_timer.start(1000*30) # 测试

    sys.exit(app.exec_())

