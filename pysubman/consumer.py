#!/usr/bin/env python
# coding=utf-8


from .connection import Connection
from .constants import DEFAULT_ADDRESS, ConsumerException
from .service import Service
from .tube import Tube


class Consumer(object):
    def __init__(self, address=DEFAULT_ADDRESS, services=None, use_threading=False):
        if (services is None
                or not isinstance(services, Service)
                or not services.get_all_services()):
            raise ConsumerException("services not empty")

        self.services = services
        self.address = address
        self.connection = Connection(self.address)
        self.use_threading = use_threading

    def tube(self, tube):
        if self.use_threading:
            from .threadtube import ThreadTube
            return ThreadTube(self, tube)
        return Tube(self, tube)
