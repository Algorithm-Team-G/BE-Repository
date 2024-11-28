import json

from entity.WorkerTaskCount import WorkerTaskCount


class Worker:
    T_NAME = "T_worker"
    C_WORKER_ID = "worker_id"
    C_WORKER_NAME = "worker_name"
    C_TEAM_ID = "team_id"
    C_JOB_ID = "job_id"
    C_CAREER = "career"
    C_MAX_TASK_COUNT = "max_task_count"

    def __init__(
            self,
            id:int,
            name:str,
            career:int,
            teamId:int,
            jobId:int,
            taskCount:int,
            maxTaskCount:int,
    ):
        self.id = id
        self.name = name
        self.career = career
        self.teamId = teamId
        self.jobId = jobId,
        self.taskCount = taskCount
        self.maxTaskCount = maxTaskCount

    @staticmethod
    def fromJson(rawData:str) -> 'Worker':
        obj = json.loads(rawData)
        return Worker(
            obj[Worker.C_WORKER_ID],
            obj[Worker.C_WORKER_NAME],
            obj[Worker.C_CAREER],
            obj[Worker.C_TEAM_ID],
            obj[Worker.C_JOB_ID],
            obj[WorkerTaskCount.C_COUNT],
            obj[Worker.C_MAX_TASK_COUNT]
        )

    def toJson(self) -> bytes:
        obj = {
            Worker.C_WORKER_ID: self.id,
            Worker.C_WORKER_NAME: self.name,
            Worker.C_CAREER: self.career,
            Worker.C_TEAM_ID: self.teamId,
            Worker.C_JOB_ID: self.jobId,
            Worker.C_MAX_TASK_COUNT: self.maxTaskCount
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')