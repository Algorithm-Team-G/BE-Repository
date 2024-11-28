import json

from entity.Task import Task
from entity.Team import Team
from exception.ValueException import DTOException


class UnassignedTaskDTO:
    def __init__(
            self,
            id:int,
            title:str,
            team:str,
    ):
        if (not isinstance(id, int) or
            not isinstance(title, str) or
            not isinstance(team, str)):
            raise DTOException("UnassignedTaskDTO", "Invalid Parameters")
        self.id = id
        self.title = title
        self.team = team

    @staticmethod
    def fromJson(data:dict):
        if (not isinstance(data.get(Task.C_TASK_ID), int)
            or not isinstance(data.get(Task.C_TASK_NAME), str)
            or not isinstance(data.get(Team.C_TEAM_NAME), str)):
            raise DTOException("UnassignedTaskDTO", "Invalid Parameters")
        return UnassignedTaskDTO(
            data[Task.C_TASK_ID],
            data[Task.C_TASK_NAME],
            data[Team.C_TEAM_NAME],
        )

    def toDict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'team': self.team,
        }