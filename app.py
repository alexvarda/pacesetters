from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "This will be the Pacesetters Projects!"


if __name__ == '__main__':
    app.run(debug=True)