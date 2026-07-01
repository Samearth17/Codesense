#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging.handlers
import configparser
import re
import time

handler = logging.handlers.TimedRotatingFileHandler(filename="test", when='s', interval=2, backupCount=5,
                                                    encoding='UTF-8')
handler.suffix = '%Y-%m-%d-%H-%M-%S.log'
handler.extMatch = re.compile(r'^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}.log$')
formatter = logging.Formatter("%(asctime)s %(message)s")
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

handler2 = logging.handlers.RotatingFileHandler(filename='test.log', maxBytes=1024, backupCount= 3)
handler2.setFormatter(formatter)
# root_logger.removeHandler(handler)
root_logger.addHandler(handler2)


def test():
    for i in range(100):
        root_logger.info("test" + str(i))
        # time.sleep(1)


def test_config():
    conf = configparser.ConfigParser()
    conf.read('config.ini', encoding='utf-8')
    name = conf.get('login', 'name')
    passwd = conf.get('login', 'password')

    if name == 'name' and passwd == 'password':
        name = input("Please input your login name: ")
        passwd = input("Please input your login password: ")
        conf.set('login', 'name', name)
        conf.set('login', 'password', passwd)
        with open('config.ini', 'w', encoding='utf-8') as f:
            conf.write(f)
    print(name)
    print(passwd)


if __name__ == '__main__':
    test_config()