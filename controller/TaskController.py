from flask import request
from flask_restx import Namespace, Resource

from dto.TaskDTO import TaskDTO
from dto.WorkerTasksDTO import WorkerTasksDTO
from service.TaskService import TaskService

TaskNamespace = Namespace('Task', description='Task related operations')

@TaskNamespace.route('/')
class TaskController(Resource):
    def post(self):
        request_json = request.get_json()
        data = TaskDTO.fromJson(request_json)
        TaskService().addTask(task=data)

@TaskNamespace.route('/assign')
class TaskAssignController(Resource):
    def get(self):
        return TaskService().getAssignedTaskList()

    def post(self):
        request_json = request.get_json()
        params = []
        for workerId, tasks in request_json.items():
            params.append(WorkerTasksDTO(workerId, tasks))
        TaskService().assignTask(params)

@TaskNamespace.route('/recommend')
class TaskRecommendController(Resource):
    def post(self):
        request_json = request.get_json()
        TaskService().recommendDistributionTasks(request_json)

@TaskNamespace.route('/unassign')
class TaskUnassignController(Resource):
    def get(self):
        return TaskService().getUnassignedTaskList()