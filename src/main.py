from pathlib import Path

from src.task_manager import TaskManager
from src.sources.file_source import FileTaskSource
from src.sources.generator_source import GeneratorTaskSource


def main():
    manager = TaskManager()

    file_task_source = FileTaskSource(Path("main.py"))
    manager.add_source(file_task_source)

    generator_task_source = GeneratorTaskSource()
    manager.add_source(generator_task_source)

    print(list(manager.get_new_tasks()))

if __name__ == "__main__":
    main()
