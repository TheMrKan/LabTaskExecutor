from typing import Protocol, Any, Iterable, runtime_checkable


class TaskInitialData(Protocol):
    """
    Данные из источника задачи для создания задачи
    """
    task_id: str
    """
    ID задачи в источнике
    """
    payload: Any
    """
    Данные для задачи. Будут переданы в обработчик.
    """


@runtime_checkable
class TaskSourceProto(Protocol):
    """
    Протокол источника задач.
    """
    name: str
    """
    ID источника задачи. Предотвращает повторное добавление источника.
    """

    def fetch_new_tasks(self) -> Iterable[TaskInitialData]:
        """
        Получает ранее не обработанные задачи из источника. Повторное чтение задачи невозможно.
        """
        ...
