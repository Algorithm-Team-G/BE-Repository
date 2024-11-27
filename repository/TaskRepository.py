from dto.request.TaskDTO import TaskDTO
from entity.Job import Job
from entity.Task import Task
from entity.Team import Team
from entity.Worker import Worker
from utils.DB import DB


class TaskRepository:
    def __init__(self):
        self.instance = DB()

    def createNewTask(self, task:TaskDTO) -> str:
        sql = f"""
            insert into {Task.T_NAME}
            (
                {Task.C_TASK_NAME},
                {Task.C_JOB_ID},
                {Task.C_START_DATE},
                {Task.C_END_DATE},
                {Task.C_IMPORTANCE}
            )
            values (
                '{task.title}',
                {task.jobId},
                '{task.begin}',
                '{task.end}',
                {task.importance}
            );"""
        count = self.instance.execute(sql)
        return f"created {count} row(s)."

    def assignTask(self, taskId:int, workerId:int) -> str:
        sql = f"""
            update {Task.T_NAME} tk
            set tk.{Task.C_WORKER_ID} = {workerId}
            where tk.{Task.C_TASK_ID} = {taskId};"""
        count = self.instance.execute(sql)
        return f"updated {count} row(s)."

    def selectAssignedTasks(self) -> dict:
        sql = f"""
            select
                tk.{Task.C_TASK_ID} task_id,
                tk.{Task.C_TASK_NAME} task_name,
                tm.{Team.C_TEAM_NAME} team_name,
                j.{Job.C_JOB_NAME} job_name,
                tk.{Task.C_START_DATE} begin,
                tk.{Task.C_END_DATE} end,
                w.{Worker.C_WORKER_NAME} worker
            from {Task.T_NAME} tk
            join {Job.T_NAME} j on tk.{Task.C_JOB_ID} = j.{Job.C_JOB_ID}
            join {Team.T_NAME} tm on j.{Job.C_TEAM_ID} = tm.{Team.C_TEAM_ID}
            join {Worker.T_NAME} w on tk.{Task.C_WORKER_ID} = w.{Worker.C_WORKER_ID}
            order by tm.{Team.C_TEAM_ID} asc, worker asc, begin asc, end asc;"""
        result = self.instance.execute(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')

    def selectUnassignedTasks(self) -> dict:
        sql = f"""
            select tk.{Task.C_TASK_ID}, tk.{Task.C_TASK_NAME}, tm.{Team.C_TEAM_NAME} team
            from {Task.T_NAME} tk
            join {Job.T_NAME} j on tk.{Task.C_JOB_ID} = j.{Job.C_JOB_ID}
            join {Team.T_NAME} tm on j.{Job.C_TEAM_ID} = tm.{Team.C_TEAM_ID}
            where tk.{Task.C_WORKER_ID} is null
            order by tk.{Task.C_TASK_ID} asc;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectTasksByTeam(self, IDList:list[int], teamId:int) -> dict:
        sql = f"""
            select
                tk.{Task.C_TASK_ID} task_id,
                tk.{Task.C_TASK_NAME} task_name,
                tm.{Team.C_TEAM_ID} team_id,
                j.{Job.C_JOB_ID} job_id,
                tk.{Task.C_START_DATE} start_date,
                tk.{Task.C_END_DATE} end_date,
                tk.{Task.C_IMPORTANCE} importance
            from {Task.T_NAME} tk
            join {Job.T_NAME} j on tk.{Task.C_JOB_ID} = j.{Job.C_JOB_ID}
            join {Team.T_NAME} tm on j.{Job.C_TEAM_ID} = tm.{Team.C_TEAM_ID}
            where tm.{Team.C_TEAM_ID} = {teamId} and tk.{Task.C_TASK_ID} in {tuple(IDList)};"""
        result = self.instance.execute(sql)
        result['start_date'] = result['start_date'].astype(str)
        result['end_date'] = result['end_date'].astype(str)
        return result.to_dict(orient='records')