#!/usr/bin/env python
# coding=utf-8

import time
import datetime
import logging
import pysubman
import random
logging.basicConfig(level=logging.DEBUG)

service = pysubman.Service()


@service.C(["EMAIL", "EMAIL.SEND_TEMPLATE"])
def handler_email_job(body):
    logging.info("start %s" % datetime.datetime.now())
    time.sleep(random.randint(1, 5))
    logging.info(("wwwwwwwww", body))
    logging.info("end %s" % datetime.datetime.now())


def main():
    consumer = pysubman.Consumer(address="192.168.0.23:11300", use_threading=True).tube("t-101")
    consumer.run(service)


if __name__ == "__main__":
    main()
