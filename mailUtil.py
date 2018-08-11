#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/6/21'
import sys
import gc
import random
import string
import json
import time
import poplib
import email
# import sys
from email import  *
from email.parser import *
from email.header import decode_header
from email.utils import parseaddr
# reload(sys)
# sys.setdefaultencoding('utf-8')
def getMail():
    # email = 'wywsun123@126.com'
    # password = 'wywsun123'
    emailard = 'lmycopper@126.com'
    password = 'lmycopper521'
    pop3_server = 'pop.126.com'

    server = poplib.POP3(pop3_server)
    # 认证:
    server.user(emailard)
    server.pass_(password)
    print('Messages: %s. Size: %s' % server.stat())
    resp, mails, octets = server.list()
    # 获取最新一封邮件, 注意索引号从1开始:
    if len(mails) == 0:
        server.quit()
        return None
    else:
        contents = []
        for n in range(1,len(mails)+1):
            resp, lines, octets = server.retr(n)
            mes = b'\r\n'.join(lines)
            msg = BytesParser().parsebytes(mes)
            cont = parserMail(msg)
            contents.append(cont)
            # server.dele(n)
        # 关闭连接:
        server.quit()
        return contents

def parserMail(msg):
    content = None
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                charst = part.get_content_charset(part)
                content = part.get_payload(decode=True)
                content = content.decode(charst)
                 # = (content.decode(charst)).split('\r\n')
    return content
