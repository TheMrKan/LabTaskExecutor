from pathlib import Path
from typing import Iterable
from dataclasses import dataclass


@dataclass
class FileTask:
    task_id: str
    payload: str


class FileTaskSource:
    """
    Источник задач из файла.
    Одна строка - одна задача.
    """
    name: str
    __filepath: Path
    __padding: int

    def __init__(self, filepath: Path):
        self.__filepath = filepath
        self.__padding = 0
        self.name = f"FileTaskSource({filepath.absolute()})"

    def fetch_new_tasks(self) -> Iterable[FileTask]:
        """
        Открывает файл, читает новые строки, закрывает.
        Новые строки определяются через padding.
        """
        with open(self.__filepath, "r") as f:
            for _ in range(self.__padding):    # пропускаем обработанные задачи
                next(f)

            for i, line in enumerate(f):
                yield FileTask(f"line{self.__padding}", line)
                self.__padding += 1
