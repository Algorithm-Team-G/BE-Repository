from common.Config import connect_db
from dto.TaskDTO import TaskDTO


class TaskRepository:
    def createNewTask(self, task:TaskDTO):
        sql = f"""
            insert into task
            values (
                '{task.title}',
                {task.jobId},
                '{task.begin}',
                '{task.end}',
                {task.importance},
                {task.level}
            );""";
        result = connect_db(sql)
        return result.to_dict(orient='records')

    def assignTask(self, taskId:int, workerId:int):
        sql = f"""
            update job j
            join task tk on j.id = tk.jobId
            set j.workerId = {workerId}
            where tk.id = {taskId};"""
        result = connect_db(sql)
        return result.to_dict(orient='records')

    def selectAssignedTasks(self):
        sql = f"""
            select tk.id, tk.name, tm.name team, j.name job, tk.begin, tk.end, w.name worker
            from task tk
            join job j on tk.jobId = j.id
            join team tm on j.teamId = tm.id
            join worker w on j.workerId = w.id
            order by tm.id asc, worker asc, tk.begin asc, tk.end asc;"""
        result = connect_db(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')

    def selectUnassignedTasks(self):
        sql = f"""
            select tk.id, tk.name, tm.name team
            from task tk
            join job j on t.jobId = j.id
            join team tm on j.teamId = tm.id
            where j.workerId is null
            order by tk.id asc;"""
        result = connect_db(sql)
        return result.to_dict(orient='records')

    def selectTaskById(self, taskId:int):
        sql = f"""
            select tk.id taskId, tk.name, tm.id teamId, j.id jobId, tk.begin, tk.end, tk.importance, tk.level
            from task tk
            join job j on tk.jobId = j.id
            join team tm on j.teamId = tm.id
            where tk.id = {taskId};"""
        result = connect_db(sql)
        result['begin'] = result['begin'].astype(str)
        result['end'] = result['end'].astype(str)
        return result.to_dict(orient='records')