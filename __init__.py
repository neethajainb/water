from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        #return 'Hello, World!'
        return jsonify({'message':'Hello, World!'})

    @app.route('/hi')
    def hi():
        return 'hello'

    @app.route('/hello')
    def hello():
        return 'hi'

    return app
