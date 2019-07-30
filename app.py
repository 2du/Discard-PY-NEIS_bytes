import re
import flask
import werkzeug.routing
import flask_compress
import flask_reggie
import tornado.ioloop
import tornado.httpserver
import tornado.wsgi

app = flask.Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if flask.request.method == 'POST':
        data = flask.request.form.get('run', '')
        s_data = data

        data = re.sub("[^ㄱ-힣]", "1", data)
        data = re.sub("[ㄱ-힣]", "3", data)

        b = 0
        for a in data:
            b += int(a)

        return '''
            ''' + str(b) + '''
            <br>
            <br>
            <form method="post">
                <textarea style="width: 100%; height: 500px;" name="run">''' + s_data + '''</textarea>
                <br>
                <br>
                <button>Input</button>
            </form>
        '''
    else:
        return '''
            <form method="post">
                <textarea style="width: 100%; height: 500px;" name="run"></textarea>
                <br>
                <br>
                <button>Input</button>
            </form>
        '''
if __name__=="__main__":
    http_server = tornado.httpserver.HTTPServer(tornado.wsgi.WSGIContainer(app))
    http_server.listen(3000, address='0.0.0.0')
    
    tornado.ioloop.IOLoop.instance().start()