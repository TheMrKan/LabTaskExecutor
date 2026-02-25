from pathlib import Path

from src.task_manager import TaskManager
from src.sources.file_source import FileTaskSource


def main():
    manager = TaskManager()
    file_task_source = FileTaskSource(Path("main.py"))
    manager.add_source(file_task_source)

    print(list(manager.get_new_tasks()))

if __name__ == "__main__":
    main()
