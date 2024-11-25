from utils.DB import DB


class TeamRepository:
    def __init__(self):
        self.instance = DB()

    def selectTeam(self) -> dict:
        sql = """
            select *
            from team tm
            order by tm.id asc;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')