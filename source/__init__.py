from flask import Flask

application = Flask(__name__)
application.secret_key = 'not very secret'
