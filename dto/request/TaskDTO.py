import json


class TaskDTO:
    def __init__(
            self,
            title:str,
            jobId:int,
            begin:str,
            end:str,
            importance:int,
    ):
        self.title = title
        self.jobId = jobId
        self.begin = begin
        self.end = end
        self.importance = importance

    @staticmethod
    def fromJson(obj:dict) -> 'TaskDTO':
        return TaskDTO(
            obj['title'],
            obj['jobId'],
            obj['begin'],
            obj['end'],
            obj['importance'],
        )