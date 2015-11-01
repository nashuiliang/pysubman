#!/usr/bin/env python
# coding=utf-8

import time
import datetime
import random
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

client = pysubman.Producer(address="192.168.0.23:11300")

while True:
    logging.info(">>> time %s" % datetime.datetime.now())
    now_time = time.time()
    client.put(EMAIL, "baidu.com", "chaungwang: {}".format(now_time))
    time.sleep(random.randint(1, 5))
