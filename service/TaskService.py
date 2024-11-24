import json

from flask import Response

from dto.request.TaskDTO import TaskDTO
from dto.request.WorkerTasksDTO import WorkerTasksDTO
from repository.TaskRepository import TaskRepository


class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def getAssignedTaskList(self) -> Response:
        result = self.repo.selectAssignedTasks()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def getUnassignedTaskList(self) -> Response:
        result = self.repo.selectUnassignedTasks()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def addTask(self, task:TaskDTO):
        self.repo.createNewTask(task)

    def assignTask(self, workerTaskList:list[WorkerTasksDTO]):
        for workerTask in workerTaskList:
            for taskId in workerTask.tasks:
                self.repo.assignTask(taskId, workerTask.workerId)

    def recommendDistributionTasks(self, tasks:list[int]):
        pass