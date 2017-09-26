from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    arr = []
    with open('data/task.csv') as fname:
        for line in fname:
            arr.append(line.rstrip().split(','))
    return render_template('home.html', info=arr)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(port=8081, debug=True)
