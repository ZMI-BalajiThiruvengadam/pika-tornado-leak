from pika import adapters
import pika


class TornadoPikaPublisher(object):
    def __init__(self, amqp_url):
        self._connection = None
        self.amqp_url = amqp_url

    def connect(self):
        return adapters.TornadoConnection(pika.URLParameters(self.amqp_url))

    def run(self):
        self._connection = self.connect()
