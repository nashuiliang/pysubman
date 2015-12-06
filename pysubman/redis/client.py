#!/usr/bin/env python
# coding=utf-8

import redis

from .publish import Publisher


class Client(object):

    def __init__(self, host):
        self._create_redis_pool(host)

    def _create_redis_pool(self, source):
        host, port, db = source.split(":")
        port = int(port)
        db = int(db)

        self.redis_pool = redis.ConnectionPool(
            host=host, port=port, db=db)

    def get_redis_client(self):
        return redis.StrictRedis(connection_pool=self.redis_pool)

    def publish(self, topic, message):
        publisher = Publisher(self)
        return publisher.publish(topic, message)
