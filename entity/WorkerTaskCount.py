import json


class WorkerTaskCount:
    T_NAME = "T_worker_task_count"
    C_WORKER_ID = "worker_id"
    C_COUNT = "count"

    def __init__(
            self,
            workerId:int,
            count:int
    ):
        self.workerId = workerId
        self.count = count

    @staticmethod
    def fromJson(rawData:str) -> 'WorkerTaskCount':
        obj = json.loads(rawData)
        return WorkerTaskCount(
            obj[WorkerTaskCount.C_WORKER_ID],
            obj[WorkerTaskCount.C_COUNT]
        )

    def toJson(self) -> bytes:
        obj = {
            WorkerTaskCount.C_WORKER_ID: self.workerId,
            WorkerTaskCount.C_COUNT: self.count
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')