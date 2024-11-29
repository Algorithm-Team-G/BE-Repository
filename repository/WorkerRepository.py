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
            select 
				w.worker_id,
                w.worker_name,
                j.team_id,
                tm.team_name,
                w.job_id,
                j.job_name,
                w.career,
                w.max_task_count,
                wtc.count
            from T_worker w
            join T_job j on w.job_id = j.job_id
            join T_team tm on j.team_id = tm.team_id
            join T_worker_task_count wtc on w.worker_id = wtc.worker_id
            where tm.team_id = {teamId}
            order by w.worker_id asc;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectActiveWorker(self, teamId:int) -> dict:
        sql = f"""
            select w.worker_id, w.worker_name
            from T_worker w
            join T_job j on w.job_id = j.job_id
            join T_worker_task_count wtc on w.worker_id = wtc.worker_id
            where j.team_id = {teamId} and wtc.count > 0"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')