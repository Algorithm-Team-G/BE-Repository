from entity.Team import Team
from utils.DB import DB


class TeamRepository:
    def __init__(self):
        self.instance = DB()

    def selectTeam(self) -> dict:
        sql = f"""
            select *
            from {Team.T_NAME} tm
            order by tm.{Team.C_TEAM_ID} asc;"""
        result = self.instance.execute(sql)
        return result.to_dict(orient='records')