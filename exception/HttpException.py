import json
from http.client import HTTPException

from flask import Response


class BadRequestException(Response):
    code = 400
    title = "Bad Request"

    def __init__(self, description: str):
        super().__init__()
        response = {
            "title": self.title,
            "description": description,
        }
        self.status = 400
        self.content_type = 'application/json; charset=utf-8'
        self.response = json.dumps(response, ensure_ascii=False)

class ServerInnerException(Response):
    code = 500
    title = "Internal Server Error"

    def __init__(self, description: str):
        super().__init__()
        response = {
            "title": self.title,
            "description": description,
        }
        self.status = 500
        self.content_type = 'application/json; charset=utf-8'
        self.response = json.dumps(response, ensure_ascii=False)