import random
from typing import Iterable
from dataclasses import dataclass


@dataclass
class GeneratedTask:
    task_id: str
    payload: float


class GeneratorTaskSource:
    """
    Источник случайных задач
    """
    name = "random"

    def fetch_new_tasks(self) -> Iterable[GeneratedTask]:
        """
        Генерирует 3 случайные задачи.
        """
        for i in range(3):
            yield GeneratedTask(f"{random.randint(1, 100)}", random.random())
