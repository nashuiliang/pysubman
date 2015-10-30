#!/usr/bin/env python
# coding=utf-8

import logging
import pysubman
logging.basicConfig(level=logging.DEBUG)

service = pysubman.Service()


@service.C(["EMAIL", "EMAIL.SEND_TEMPLATE"])
def handler_email_job(body):
    logging.warn(("wwwwwwwww", body))


def main():
    consumer = pysubman.Consumer(beanstalkd_host="192.168.0.23:11300",
                                 services=service).tube("t-101")
    consumer.run()


if __name__ == "__main__":
    main()
