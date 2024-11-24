import json


class UnassignedTaskDTO:
    def __init__(
            self,
            id:int,
            title:str,
            team:str,
    ):
        self.id = id
        self.title = title
        self.team = team

    def toJson(self) -> bytes:
        obj = {
            'id': self.id,
            'title': self.title,
            'team': self.team,
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')