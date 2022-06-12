from crypt import methods
from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@route('/', methods=['GET', 'POST'])
def index():
    return "Starting Machine Learning Project"

if __name__ == '__main__':
    app.run(debug=True)