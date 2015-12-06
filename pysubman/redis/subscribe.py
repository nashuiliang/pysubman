#!/usr/bin/env python
# coding=utf-8


class Subscriber(object):

    def __init__(self, client):
        self.client = client

    def subscribe(self, topic, message):
        sub_count = self._publish(topic, message)
        if sub_count == 0:
            self._lpush(topic, message)
            return 1
        return sub_count

    def _publish(self, topic, message):
        return self.client.get_redis_client().publish(topic, message)

    def _lpush(self, topic, message):
        return self.client.get_redis_client().lpush(topic, message)
