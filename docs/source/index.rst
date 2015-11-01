.. pysubman documentation master file, created by
   sphinx-quickstart on Sun Nov  1 16:29:07 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pysubman's documentation!
====================================

Demo(consumer)
--------------

消费者简单例子::

    #!/usr/bin/env python
    # coding=utf-8

    import logging
    import pysubman
    logging.basicConfig(level=logging.DEBUG)

    service = pysubman.Service()


    @service.C(["EMAIL", "EMAIL.SEND_TEMPLATE"])
    def handler_email_job(body):
        logging.warn(("body", body))


    def main():
        consumer = pysubman.Consumer(address="192.168.0.23:11300").tube("t-101")
        consumer.run(services)


    if __name__ == "__main__":
        main()


Demo(publish)
-------------

生产者简单例子::

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

    client = pysubman.Producer(address="192.168.0.23:11300")

    while True:
        now_time = time.time()
        client.put(EMAIL, "baidu.com", "chaungwang: {}".format(now_time))
        time.sleep(10)


安装
----

**自动安装**::

    pip install pysubman


文档
----

.. toctree::
   :titlesonly:

   consumer

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
