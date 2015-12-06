#!/usr/bin/env python
# coding=utf-8

import logging
logging.basicConfig(level=logging.DEBUG)
from .client import Client
import unittest


class TestPublish(unittest.TestCase):
    def setUp(self):
        self.client = Client(host="192.168.0.236:36379:5")

    def tearDown(self):
        self.client.close()

    def test_publish(self):
        import json
        message = json.loads({
            "relation_token": "123123qweqewqeqweqw",
            "info": {"email": "592030542@qq.com"}})
        sub_count = self.client.publish(topic="oauth:linkedin", message=message)
        logging.warn(sub_count)


if __name__ == "__main__":
    unittest.main()
