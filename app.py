from flask import Flask

app = Flask(__name__)

@app.route("/ping")
def hello_world():
    return {'status': 'good!'}
if __name__ == '__main__':
    app.run(debug=True)