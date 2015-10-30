#!/usr/bin/env python
# coding=utf-8

import time
import logging
logging.basicConfig(level=logging.DEBUG)
import pysubman


class EMAIL(object):
    Tube = "t-101"
    Topic = "EMAIL"
    Info = [
        ("TemplateUrl", "%s"),
        ("Params", "%s"),
    ]

client = pysubman.Producer(beanstalkd_host="192.168.0.23:11300")

while True:
    now_time = time.time()
    client.put(EMAIL, "baidu.com", "chaungwang: {}".format(now_time))
    time.sleep(1)
