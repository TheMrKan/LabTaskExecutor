import pytest
from unittest.mock import Mock, create_autospec

from src.task_manager import TaskManager, InvalidTaskSourceError
from src.api import TaskSourceProto, TaskInitialData


def test_add_valid_source():
    manager = TaskManager()
    valid_source = create_autospec(TaskSourceProto)
    valid_source.name = "valid_source"

    manager.add_source(valid_source)

    assert "valid_source" in manager._TaskManager__sources
    assert manager._TaskManager__sources["valid_source"] is valid_source


def test_add_duplicate_source():
    manager = TaskManager()
    source = create_autospec(TaskSourceProto)
    source.name = "duplicate_source"

    manager.add_source(source)

    with pytest.raises(KeyError, match="Source duplicate_source already added"):
        manager.add_source(source)


def test_add_invalid_source():
    """Проверяет, что добавление объекта, не соответствующего TaskSourceProto, вызывает InvalidTaskSourceError."""
    manager = TaskManager()
    invalid_source = Mock()
    # Не реализует TaskSourceProto

    with pytest.raises(InvalidTaskSourceError):
        manager.add_source(invalid_source)


def test_get_new_tasks_returns_combined_tasks():
    manager = TaskManager()

    task1 = Mock(spec=TaskInitialData)
    task1.task_id = "task1"
    task1.payload = "payload1"

    task2 = Mock(spec=TaskInitialData)
    task2.task_id = "task2"
    task2.payload = "payload2"

    source1 = create_autospec(TaskSourceProto)
    source1.name = "source1"
    source1.fetch_new_tasks.return_value = [task1]

    source2 = create_autospec(TaskSourceProto)
    source2.name = "source2"
    source2.fetch_new_tasks.return_value = [task2]

    manager.add_source(source1)
    manager.add_source(source2)

    tasks = list(manager.get_new_tasks())

    assert len(tasks) == 2
    assert tasks[0] is task1
    assert tasks[1] is task2
    source1.fetch_new_tasks.assert_called_once()
    source2.fetch_new_tasks.assert_called_once()
