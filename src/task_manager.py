from typing import Any, Iterable

from src.api import TaskSourceProto, TaskInitialData


class InvalidTaskSourceError(Exception):
    pass


class TaskManager:

    __sources: dict[str, TaskSourceProto]

    def __init__(self):
        self.__sources = {}

    def add_source(self, source: TaskSourceProto):
        self.__assert_source_proto(source)
        self.__assert_not_added(source)

        self.__sources[source.name] = source

    @staticmethod
    def __assert_source_proto(obj: Any):
        if not isinstance(obj, TaskSourceProto):
            raise InvalidTaskSourceError

    def __assert_not_added(self, source: TaskSourceProto):
        if source.name in self.__sources.keys():
            raise KeyError(f"Source {source.name} already added")

    def get_new_tasks(self) -> Iterable[TaskInitialData]:
        """
        Временный метод для тестирования
        """
        for source in self.__sources.values():
            yield from source.fetch_new_tasks()
