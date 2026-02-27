from urllib.parse import urlparse
from collections import namedtuple
import json
from typing import Iterable


APITask = namedtuple('APITask', ['task_id', 'payload'])


class APITaskSource:
    """
    Источник задач из HTTP эндпоинта
    """
    name: str
    __url: str

    def __init__(self, url: str):
        self.__url = url
        self.name = urlparse(url).hostname or url

    def fetch_new_tasks(self) -> Iterable[APITask]:
        # здесь http запрос
        parsed = json.loads('[{"task_id": "a", "payload": {}}, {"task_id": "b", "payload": {}}, {"task_id": "c", "payload": {}}]')
        for task in parsed:
            yield APITask(**task)
