import tornado
import tornado.ioloop
import tornado.web
import tornado.template

from web.lib import get_pardir


class MainHandler(tornado.web.RequestHandler):

    def get(self):

        if not self.current_user:
            # route = os.path.realpath(os.path.join(self.__file__, os.pardir))
            self.render(get_pardir() + '/templates/login.html')
            return


class Login(tornado.web.RequestHandler):

    def get(self):

        user = self.get_argument('user')
        pwd = self.get_argument('pwd')


class Form(tornado.web.RequestHandler):
    pass


class Organ(tornado.web.RequestHandler):
    pass


class Graphs(tornado.web.RequestHandler):
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
    app.listen(8898)
    tornado.ioloop.IOLoop.current().start()