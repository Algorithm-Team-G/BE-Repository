
class Worker:
    def __init__(
            self,
            id:int,
            name:str,
            organization_id:int,
            job_id:int,
            career:int
    ):
        self.id = id
        self.name = name
        self.organization_id = organization_id
        self.job_id = job_id
        self.career = career