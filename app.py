from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World from Flask App'

@app.route('/parse_url')
def parse():
    return 'Retrieving requested HTML content...'

if __name__ == '__main__':
    app.run()