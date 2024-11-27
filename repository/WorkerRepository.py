from repository.TeamRepository import TeamRepository
from utils.DB import DB


class WorkerRepository:
    def __init__(self):
        self.instance = DB()

    def selectFreeWorkersByTeam(self, teamId:int) -> dict:
        sql = f"""
            select *
            from T_worker w
            where w.team_id = {teamId}
            order by w.team_id asc;"""
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