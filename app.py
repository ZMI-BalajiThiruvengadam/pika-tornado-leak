import signal
import tornado.gen
import tornado.ioloop
import tornado.web
from guppy import hpy
from lib.TornadoPikaPublisher import TornadoPikaPublisher

hp = hpy()


class FreezeHandler(tornado.web.RequestHandler):
    def get(self):
        hp.setrelheap()


class GarbageHandler(tornado.web.RequestHandler):
    def get(self):
        print hp.heap()


def make_app():
    """Return the Tornado Application object."""
    return tornado.web.Application([
        (r'/freeze', FreezeHandler),
        (r'/garbage', GarbageHandler)
    ])


def sig_handler(sig, frame):
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(shutdown)


def shutdown():
    io_loop = tornado.ioloop.IOLoop.instance()
    io_loop.stop()


def rmq_init():
    rmq = TornadoPikaPublisher('amqp://guest:guest@rmq:5672/%2F')
    rmq.run()


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, sig_handler)

    # Connect to RMQ
    rmq_init()

    # Set up the Tornado application object
    app = make_app()
    app.listen(8000)

    ioloop_instance = tornado.ioloop.IOLoop.current().start()
