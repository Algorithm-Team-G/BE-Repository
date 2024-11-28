from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from controller.TaskController import TaskNamespace

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

api = Api(app)
api.add_namespace(TaskNamespace, "/task")

if __name__ == '__main__':
    app.run()