import json


class Worker:
    def __init__(
            self,
            id:int,
            name:str,
            career:int,
            teamId:int,
            jobId:int,
            taskCount:int,
            maxTaskCount:int,
            copied:int=0
    ):
        self.id = id
        self.name = name
        self.career = career
        self.teamId = teamId
        self.jobId = jobId,
        self.taskCount = taskCount
        self.maxTaskCount = maxTaskCount
        self.copied = copied

    @staticmethod
    def fromJson(rawData:str) -> 'Worker':
        obj = json.loads(rawData)
        return Worker(
            obj['id'],
            obj['name'],
            obj['career'],
            obj['teamId'],
            obj['jobId'],
            obj['taskCount'],
            obj['maxTaskCount'],
            0
        )

    def toJson(self) -> bytes:
        obj = {
            'id': self.id,
            'name': self.name,
            'career': self.career,
            'teamId': self.teamId,
            'jobId': self.jobId,
            'taskCount': self.taskCount,
            'maxTaskCount': self.maxTaskCount
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')