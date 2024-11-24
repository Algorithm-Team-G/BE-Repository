import json


class TaskDTO:
    def __init__(
            self,
            title:str,
            jobId:int,
            begin:str,
            end:str,
            importance:int,
            level:int,
    ):
        self.title = title
        self.jobId = jobId
        self.begin = begin
        self.end = end
        self.importance = importance
        self.level = level

    @staticmethod
    def fromJson(rawData:str) -> 'TaskDTO':
        obj = json.loads(rawData)
        return TaskDTO(
            obj['title'],
            obj['jobId'],
            obj['begin'],
            obj['end'],
            obj['importance'],
            obj['level']
        )

    def toJson(self) -> bytes:
        obj = {
            'title': self.title,
            'jobId': self.jobId,
            'begin': self.begin,
            'end': self.end,
            'importance': self.importance,
            'level': self.level
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')