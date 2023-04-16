import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    someVarFromEnv = os.environ.get('someVar')
    return 'This is a testing app.\nMy environment variable is: {}!\n'.format(someVarFromEnv)

if __name__ == "__main__":
    app.debug = True
    app.host='0.0.0.0'
    app.port=int(os.environ.get('PORT', 8080))
    app.run()
