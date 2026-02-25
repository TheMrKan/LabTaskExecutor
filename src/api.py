from typing import Protocol, Any, Iterable, runtime_checkable


class TaskInitialData(Protocol):
    task_id: str
    payload: Any


@runtime_checkable
class TaskSourceProto(Protocol):
    name: str

    def fetch_new_tasks(self) -> Iterable[TaskInitialData]:
        ...
