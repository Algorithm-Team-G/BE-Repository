import json


class _AssignedTaskDTO:
    def __init__(
            self,
            id: str,
            title: str,
            begin: str,
            duration: int,
    ):
        self.id = id
        self.title = title
        self.begin = begin
        self.duration = duration

    def toJson(self) -> bytes:
        obj = {
            'id': self.id,
            'title': self.title,
            'begin': self.begin,
            'duration': self.duration
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')


class _AssignedTasksForWorkerDTO:
    def __init__(
            self,
            workerId: int,
            workerName: str,
            tasks: list[_AssignedTaskDTO]
    ):
        self.workerId = workerId
        self.workerName = workerName
        self.tasks = tasks

    def toJson(self) -> bytes:
        obj = {
            "name": self.workerName,
            "tasks": [task.toJson() for task in self.tasks]
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')


class _TeamOfWorkersDTO:
    def __init__(
            self,
            teamId: int,
            teamName: str,
            workers: dict[int,_AssignedTasksForWorkerDTO]
    ):
        self.teamId = teamId
        self.teamName = teamName
        self.workers = workers

    def toJson(self) -> bytes:
        obj = {
            "name": self.teamName,
            "workers": {
                workerId: worker.toJson() for workerId, worker in self.workers.items()
            }
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')


class TaskDistributionDTO:
    def __init__(self, teamOfWorker: dict[int,_TeamOfWorkersDTO]):
        self.teamOfWorker = teamOfWorker

    def toJson(self):
        obj = {}
        for teamId, value in self.teamOfWorker.items():
            obj[teamId] = value.toJson()
        return json.dumps(obj, ensure_ascii=False).encode('utf8')
