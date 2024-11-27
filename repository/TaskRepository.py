from dto.request.TaskDTO import TaskDTO
from utils.DB import DB


class TaskRepository:
    def __init__(self):
        self.instance = DB()

    def createNewTask(self, task:TaskDTO) -> str:
        sql = f"""
            insert into T_task (task_name, start_date, end_date, importance, worker_id)
            values (
                '{task.title}',
                {task.jobId},begin
                '{task.begin}',end
                '{task.end}',importance
                {task.importance},job
                {task.level}
            );"""
        count = self.instance.execute(sql)
        return f"created {count} row(s)."

    def assignTask(self, taskId:int, workerId:int) -> str:
        sql = f"""
            update job j
            join task tk on j.id = tk.jobId
            set j.workerId = {workerId}
            where tk.id = {taskId};"""
        count = self.instance.execute(sql)
        return f"updated {count} row(s)."

    def selectAssignedTasks(self) -> dict:
        sql = f"""
            select ta.task_id, ta.task_name, t.team_name, j.job_name, ta.start_date, ta.end_date, w.worker_name from T_task ta
        join T_worker w on ta.worker_id = w.worker_id
        join T_job j on w.job_id = j.job_id
        join T_team t on j.team_id = t.team_id
        order by t.team_id asc, w.worker_name asc, ta.start_date asc, ta.end_date asc;
        """
        result = self.instance.execute(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')

    def selectUnassignedTasks(self) -> dict:
        sql = f"""
            select * from T_task ta
            join T_job j on ta.job_id = j.job_id
            join T_team tm on j.team_id = tm.team_id
            where ta.worker_id is null
            order by ta.task_id asc;
"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectTasksByTeam(self, IDList:list[int], teamId:int) -> dict:
        sql = f"""
            select * from T_task ta
            join T_job j on ta.job_id = j.job_id
            join T_team t on j.team_id = t.team_id
            where t.team_id = {teamId} and ta.task_id in {tuple(IDList)};
"""
        
        result = self.instance.execute(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')