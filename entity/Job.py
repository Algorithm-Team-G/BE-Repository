
class Job:
    T_NAME = "T_job"
    C_JOB_ID = "job_id"
    C_JOB_NAME = "job_name"
    C_TEAM_ID = "team_id"

    def __init__(self, id:int, name:str, teamId:int):
        self.id = id
        self.name = name
        self.teamId = teamId