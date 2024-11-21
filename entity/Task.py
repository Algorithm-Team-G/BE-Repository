
class Task:
    def __init__(
            self,
            id:int,
            name:str,
            jobId:int,
            start:str,
            end:str,
            exceptTime:int,
            importance:int,
            level:int,
            workerId:int
    ):
        self.id = id
        self.name = name
        self.jobId = jobId
        self.start = start
        self.end = end
        self.exceptTime = exceptTime
        self.importance = importance
        self.level = level
        self.workerId = workerId