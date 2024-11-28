from flask import request, Response
from flask_restx import Namespace, Resource

from dto.request.TaskDTO import TaskDTO
from dto.request.WorkerTasksDTO import WorkerTasksDTO
from exception.HttpException import BadRequestException
from exception.ValueException import DTOException
from service.TaskService import TaskService

TaskNamespace = Namespace('Task', description='Task related operations')

@TaskNamespace.route('/')
class TaskController(Resource):
    def post(self):
        try:
            request_json = request.get_json()
            data = TaskDTO.fromJson(request_json)
            return TaskService().addTask(task=data)
        except DTOException as e:
            return BadRequestException(e.message)

@TaskNamespace.route('/assign')
class TaskAssignController(Resource):
    def get(self):
        return TaskService().getAssignedTaskList()

    def post(self):
        try:
            request_json = request.get_json()
            params = []
            for workerId, tasks in request_json.items():
                params.append(WorkerTasksDTO(int(workerId), tasks))
            return TaskService().assignTask(params)
        except DTOException as e:
            return BadRequestException(e.message)

@TaskNamespace.route('/recommend')
class TaskRecommendController(Resource):
    def post(self):
        try:
            request_json = request.get_json()
            for taskId in request_json:
                if not isinstance(taskId, int):
                    raise DTOException('tasks', 'Invalid Parameters')
            return TaskService().recommendDistributionTasks(request_json)
        except DTOException as e:
            return BadRequestException(e.message)


@TaskNamespace.route('/unassign')
class TaskUnassignController(Resource):
    def get(self):
        return TaskService().getUnassignedTaskList()
