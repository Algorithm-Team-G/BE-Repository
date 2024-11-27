
class Team:
    T_NAME = "T_team"
    C_TEAM_ID = "team_id"
    C_TEAM_NAME = "team_name"

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name