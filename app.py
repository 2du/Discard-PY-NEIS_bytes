import re
import flask
app = flask.Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if flask.request.method == 'POST':
        data = flask.request.form.get('run', '')
        print(data)
        s_data = data

        data = re.sub("[^ㄱ-힣]", "1", data)
        data = re.sub("[ㄱ-힣]", "3", data)

        b = 0
        print(data)
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

if __name__ == '__main__':
    app.run(debug = True)