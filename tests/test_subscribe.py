#!/usr/bin/env python
# coding=utf-8

import logging
logging.basicConfig(level=logging.DEBUG)

import os
import sys
sys.path.append(os.path.abspath(".."))

from pysubman.redis.service import Service
from pysubman.redis.client import Client
from pysubman.redis.subscribe import Subscriber
services = Service()


@services.C("oauth:linkedin")
def handler_linkedin_service(message, **kwargs):
    raise KeyError(message)


if __name__ == "__main__":
    Subscriber(Client(host="192.168.0.236:36379:5")).subscribe(services)
