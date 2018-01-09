import tornado
import tornado.ioloop
import tornado.web
import tornado.template


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        pass


class Login:
    pass


class Form:
    pass


class Organ:
    pass


class Graphs:
    pass


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", Login),
        (r"/administration", Form),
        (r"/organigrama", Organ),
        (r"/graphs", Graphs)
    ])


if __name__ == "__main__":

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()