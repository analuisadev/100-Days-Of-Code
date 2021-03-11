from flask import Flask #importação do flask

app = Flask(__name__) #instancia do flask

from app.controllers import default
