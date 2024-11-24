import json


class Task:
    def __init__(
            self,
            id:int,
            name:str,
            jobId:int,
            begin:str,
            end:str,
            importance:int,
            level:int,
            workerId:int
    ):
        self.id = id
        self.name = name
        self.jobId = jobId
        self.begin = begin
        self.end = end
        self.importance = importance
        self.level = level
        self.workerId = workerId

    @staticmethod
    def fromJson(rawData:str) -> 'Task':
        obj = json.loads(rawData)
        return Task(
            obj['id'],
            obj['name'],
            obj['jobId'],
            obj['begin'],
            obj['end'],
            obj['importance'],
            obj['level'],
            obj['workerId']
        )

    def toJson(self) -> bytes:
        obj = {
            'id': self.id,
            'name': self.name,
            'jobId': self.jobId,
            'begin': self.begin,
            'end': self.end,
            'importance': self.importance,
            'level': self.level,
            'workerId': self.workerId
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')