import tornado.ioloop
import tornado.web
import spacyServer

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        sentence = self.get_argument("sentence")
        tokens = spacyServer.main(sentence)
        self.write(tokens.encode('utf-8'))

def app():
    return tornado.web.Application([
        (r"/",MainHandler),
		(r"/static/(.*)",tornado.web.StaticFileHandler,{'path' : 'static'}),
    ])

if __name__ == "__main__":
    app = app()
    app.listen(9663)
    tornado.ioloop.IOLoop.current().start()