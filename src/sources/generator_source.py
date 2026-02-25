import random
from typing import Iterable
from dataclasses import dataclass


@dataclass
class GeneratedTask:
    task_id: str
    payload: float


class GeneratorTaskSource:
    name = "random"

    def fetch_new_tasks(self) -> Iterable[GeneratedTask]:
        for i in range(3):
            yield GeneratedTask(f"{random.randint(1, 100)}", random.random())
