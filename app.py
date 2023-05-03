from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hello, Olá Beto oi José !!</h2>"


if __name__ == '__main__':
    app.run(debug=True)
