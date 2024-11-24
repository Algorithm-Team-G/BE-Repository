import json


class WorkerTasksDTO:
    def __init__(self, workerId:int, tasks:list[int]):
        self.workerId = workerId
        self.tasks = tasks

    @staticmethod
    def fromJson(rawData:str) -> 'WorkerTasksDTO':
        obj = json.loads(rawData)
        return WorkerTasksDTO(
            obj['workerId'],
            obj['tasks']
        )