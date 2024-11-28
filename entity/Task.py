import json
from datetime import datetime

from utils.DateFormat import DateFormat


class Task:
    T_NAME = "T_task"
    C_TASK_ID = "task_id"
    C_TASK_NAME = "task_name"
    C_TEAM_ID = "team_id"
    C_JOB_ID = "job_id"
    C_START_DATE = "start_date"
    C_END_DATE = "end_date"
    C_IMPORTANCE = "importance"
    C_WORKER_ID = "worker_id"

    def __init__(
            self,
            id:int,
            name:str,
            teamId:int,
            jobId:int,
            begin:datetime,
            end:datetime,
            importance:int,
            workerId:int=None
    ):
        self.id = id
        self.name = name
        self.teamId = teamId
        self.jobId = jobId
        self.begin = begin
        self.end = end
        self.importance = importance
        self.workerId = workerId

    @staticmethod
    def fromJson(rawData:str) -> 'Task':
        obj = json.loads(rawData)
        workerId = obj.get(Task.C_WORKER_ID)
        return Task(
            obj[Task.C_TASK_ID],
            obj[Task.C_TASK_NAME],
            obj[Task.C_TEAM_ID],
            obj[Task.C_JOB_ID],
            DateFormat.parse(obj[Task.C_START_DATE]),
            DateFormat.parse(obj[Task.C_END_DATE]),
            obj[Task.C_IMPORTANCE],
            workerId
        )

    def toJson(self) -> bytes:
        obj = {
            Task.C_TASK_ID: self.id,
            Task.C_TASK_NAME: self.name,
            Task.C_JOB_ID: self.jobId,
            Task.C_START_DATE: DateFormat.format(self.begin),
            Task.C_END_DATE: DateFormat.format(self.end),
            Task.C_IMPORTANCE: self.importance,
            Task.C_WORKER_ID: self.workerId
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')