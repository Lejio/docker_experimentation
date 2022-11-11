from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/test')
def test():
    return 'Test, Test'


if __name__ == "__main__":

    app.run()