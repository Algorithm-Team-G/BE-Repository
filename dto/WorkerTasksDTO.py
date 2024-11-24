
class WorkerTasksDTO:
    def __init__(self, workerId:int, tasks:list[int]):
        self.workerId = workerId
        self.tasks = tasks