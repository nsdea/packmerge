import merger

import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    form = flask.request.form.to_dict()
    files = flask.request.files
    
    print(request.files)

    merger.merge(input_zips=None, reverse=form.get('reversed') == 'on')

    return flask.send_file('../output.zip')

@app.route('/download', )
def download():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2121, debug=True)
    app.config['UPLOAD_FOLDER'] = 'uploaded/'