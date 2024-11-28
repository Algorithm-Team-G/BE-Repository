import json

from exception.ValueException import DTOException


class WorkerTasksDTO:
    def __init__(self, workerId:int, tasks:list[int]):
        if (workerId is None
            or tasks is None
            or not isinstance(workerId, int)
            or not isinstance(tasks, list)
            or not all(isinstance(task, int) for task in tasks)):
            raise DTOException('WorkerTaskDTO', 'Invalid Parameters')
        self.workerId = workerId
        self.tasks = tasks