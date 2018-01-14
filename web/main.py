import tornado
import tornado.ioloop
import tornado.web
import tornado.template
from sqlalchemy import create_engine


__engine__ = create_engine('mysql+mysqldb://admin:Abc123$@localhost/db')

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


class Form(tornado.web.RequestHandler):
    pass


class Graphs(tornado.web.RequestHandler):
    pass


class Organ(tornado.web.RequestHandler):

    def get(self):

        connection = __engine__.connect()
        query = 'SELECT ID, NAME, DEPARTMENT, CHARGE, MANAGER_ID FROM EMPLOYEE ' \
                'ORDER BY DEPARTMENT, CHARGE ASC'
        result = connection.execute(query)
        organ = {}

        for row in result:

            id = row[0]
            name = row[1]
            department = row[2]
            charge = row[3]
            manager_id = row[4]

            if department not in organ:
                organ[department] = {id: {'name': name,
                                          'charge': charge,
                                          'responsible': manager_id,
                                          'subordinates': {}
                                          }
                                     }
            else:
                for boss, data in organ[department].iteritems():
                    if boss == manager_id:
                        organ[department][manager_id]['subordinates'][id] = {
                            'name': name,
                            'charge': charge,
                            'responsible': manager_id,
                            'subordinates': {}
                        }
                        break
                    # buscar entre subordinados
                    else:
                        sub_bosses = data['subordinates']
                        for boss_id in sub_bosses:
                            if boss_id == manager_id:
                                organ[department][manager_id]['subordinates'][id] = {
                                    'name': name,
                                    'charge': charge,
                                    'responsible': manager_id,
                                    'subordinates': {}
                                }
                                break
                # nadie es su jefe
                else:
                    organ[department][id] = {
                        'name': name,
                        'charge': charge,
                        'responsible': manager_id,
                        'subordinates': {}
                    }

        # organ is built at this point
        self.render(get_pardir() + '/templates/organ.html')


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
    app.listen(8898)
    tornado.ioloop.IOLoop.current().start()