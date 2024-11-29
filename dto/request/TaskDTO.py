from exception.ValueException import DTOException


class TaskDTO:
    def __init__(
            self,
            title:str,
            jobId:int,
            begin:str,
            end:str,
            level:int,
            importance:int,
    ):
        if (not isinstance(title, str)
            or not isinstance(jobId, int)
            or not isinstance(begin, str)
            or not isinstance(end, str)
            or not isinstance(level, int)
            or not isinstance(importance, int)):
            raise DTOException('TaskDTO', 'Invalid Parameters')
        self.title = title
        self.jobId = jobId
        self.begin = begin
        self.end = end
        self.level = level
        self.importance = importance

    @staticmethod
    def fromJson(obj:dict) -> 'TaskDTO':
        if (obj is None
            or not isinstance(obj.get("begin"), str)
            or not isinstance(obj.get("end"), str)
            or not isinstance(obj.get("importance"), int)
            or not isinstance(obj.get("jobId"), int)
            or not isinstance(obj.get("level"), int)
            or not isinstance(obj.get("title"), str)):
            raise DTOException("TaskDTO", "Invalid Parameters")
        return TaskDTO(
            obj['title'],
            obj['jobId'],
            obj['begin'],
            obj['end'],
            obj['level'],
            obj['importance'],
        )