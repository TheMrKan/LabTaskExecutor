from typing import Any, Iterable

from src.api import TaskSourceProto, TaskInitialData


class InvalidTaskSourceError(Exception):
    """
    Объект не является источником задач
    """
    pass


class TaskManager:
    """
    Класс для управления задачами и источниками.
    Временное решение для тестирования, позже будет переработан.
    """

    __sources: dict[str, TaskSourceProto]

    def __init__(self):
        self.__sources = {}

    def add_source(self, source: TaskSourceProto):
        """
        Добавляет источник.
        Повторное добавление того же источника вызовет KeyError.
        :return:
        """
        self.__assert_valid_source(source)
        self.__assert_not_added(source)

        self.__sources[source.name] = source

    @staticmethod
    def __assert_valid_source(obj: Any):
        """
        Вызывает InvalidTaskSourceError, если объект не выполняет контракт источника задач
        """
        if not isinstance(obj, TaskSourceProto):
            raise InvalidTaskSourceError

    def __assert_not_added(self, source: TaskSourceProto):
        """
        Вызывает KeyError, если
        """
        if source.name in self.__sources.keys():
            raise KeyError(f"Source {source.name} already added")

    def get_new_tasks(self) -> Iterable[TaskInitialData]:
        """
        Временный метод для тестирования.
        Получает новые задачи из всех добавленных источников.
        """
        for source in self.__sources.values():
            yield from source.fetch_new_tasks()
