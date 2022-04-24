from words import generateWord
import flask
app = flask.Flask(__name__)

@app.route('/')
def test():
    return generateWord(5)

if __name__ == "__main__":
    app.run()