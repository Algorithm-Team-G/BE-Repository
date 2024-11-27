from entity.Job import Job
from entity.Team import Team
from entity.Worker import Worker
from entity.WorkerTaskCount import WorkerTaskCount
from repository.TeamRepository import TeamRepository
from utils.DB import DB


class WorkerRepository:
    def __init__(self):
        self.instance = DB()

    def selectFreeWorkersByTeam(self, teamId:int) -> dict:
        sql = f"""
            select *
            from {Worker.T_NAME} w
            join {Job.T_NAME} j on w.{Worker.C_JOB_ID} = j.{Job.C_JOB_ID}
            join {Team.T_NAME} tm on j.{Job.C_TEAM_ID} = tm.{Team.C_TEAM_ID}
            join {WorkerTaskCount.T_NAME} wtc on w.{Worker.C_WORKER_ID} = wtc.{Worker.C_WORKER_ID}
            where tm.{Team.C_TEAM_ID} = {teamId}
            order by w.{Worker.C_WORKER_ID} asc;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    # def assignTask(self, taskId:int, workerId:int) -> str:
    #     sql = f"""
    #         update worker w
    #         join task tk on j.id = tk.jobId
    #         set j.workerId = {workerId}
    #         where tk.id = {taskId};"""
    #     count = self.instance.execute(sql)
    #     return f"updated {count} row(s)."

    # def depriveTask(self, taskId:int, workerId:int) -> str:
    #     sql = f"""
    #         update job j
    #         join task tk on j.id = tk.jobId
    #         set j.workerId = null
    #         where tk.id = {taskId};"""
    #     count = self.instance.execute(sql)
    #     return f"updated {count} row(s)."