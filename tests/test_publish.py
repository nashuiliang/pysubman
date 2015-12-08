#!/usr/bin/env python
# coding=utf-8

import logging
logging.basicConfig(level=logging.DEBUG)
import os
import sys
sys.path.append(os.path.abspath(".."))
logging.warn(sys.path)

from pysubman.redis.client import Client
import json
import string
import random
import time
import threading


_Threading_Exit = False


def _threading_exit(signum, frame):
    global _Threading_Exit
    print "Ctrl-C.... Exiting"

    _Threading_Exit = True


def worker():
    client = Client(host="192.168.0.236:36379:5")

    i = 1
    while not _Threading_Exit:
        now_time = time.time()
        message = json.dumps({
            "type": u"王创z",
            "time": now_time,
            "num": i,
            #"info": "".join([random.choice(string.ascii_letters) for k in xrange(100)])
        })
        i = i + 1
        result = client.publish("oauth:linkedin", message)
        logging.warn((now_time, result, i))
        time.sleep(random.randint(1, 3))


def main():
    tubes = []
    for i in xrange(1):
        t = threading.Thread(target=worker)
        t.start()
        tubes.append(t)

    while len(tubes) > 0:
        threads = []
        for k in tubes:
            if k is not None and k.isAlive():
                k.join(1)
                threads.append(k)
        tubes = threads
    logging.warn(" end ! ")


if __name__ == "__main__":
    main()
