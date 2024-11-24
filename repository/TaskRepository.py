from dto.request.TaskDTO import TaskDTO
from utils.DB import DB


class TaskRepository:
    def __init__(self):
        self.instance = DB()

    def createNewTask(self, task:TaskDTO) -> str:
        sql = f"""
            insert into task
            values (
                '{task.title}',
                {task.jobId},
                '{task.begin}',
                '{task.end}',
                {task.importance},
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
            select tk.id, tk.name, tm.name team, j.name job, tk.begin, tk.end, w.name worker
            from task tk
            join job j on tk.jobId = j.id
            join team tm on j.teamId = tm.id
            join worker w on j.workerId = w.id
            order by tm.id asc, worker asc, tk.begin asc, tk.end asc;"""
        result = self.instance.execute(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')

    def selectUnassignedTasks(self) -> dict:
        sql = f"""
            select tk.id, tk.name, tm.name team
            from task tk
            join job j on t.jobId = j.id
            join team tm on j.teamId = tm.id
            where j.workerId is null
            order by tk.id asc;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')

    def selectTasksByIDs(self, IDList:list[int]) -> dict:
        sql = f"""
            select tk.id taskId, tk.name, tm.id teamId, j.id jobId, tk.begin, tk.end, tk.importance, tk.level
            from task tk
            join job j on tk.jobId = j.id
            join team tm on j.teamId = tm.id
            where tk.id in {tuple(IDList)};"""
        result = self.instance.execute(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')