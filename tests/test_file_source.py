import pytest

from src.sources.file_source import FileTaskSource, FileTask

class TestFileTaskSource:
    @pytest.fixture
    def temp_file(self, tmp_path):
        f = tmp_path / "tasks.txt"
        f.write_text("task1\ntask2\ntask3\n")
        return f

    def test_name(self, temp_file):
        source = FileTaskSource(temp_file)
        assert source.name == f"FileTaskSource({temp_file.absolute()})"

    def test_read_tasks(self, temp_file):
        source = FileTaskSource(temp_file)
        tasks = list(source.fetch_new_tasks())

        assert len(tasks) == 3
        assert isinstance(tasks[0], FileTask)
        assert tasks[0].task_id == "line0"
        assert tasks[0].payload == "task1\n"
        assert tasks[1].task_id == "line1"
        assert tasks[1].payload == "task2\n"
        assert tasks[2].task_id == "line2"
        assert tasks[2].payload == "task3\n"

    def test_padding(self, temp_file):
        source = FileTaskSource(temp_file)

        first_tasks = list(source.fetch_new_tasks())
        assert len(first_tasks) == 3

        second_tasks = list(source.fetch_new_tasks())
        assert len(second_tasks) == 0

        temp_file.write_text("task1\ntask2\ntask3\ntask4\ntask5\n")

        third_tasks = list(source.fetch_new_tasks())
        assert len(third_tasks) == 2
        assert third_tasks[0].task_id == "line3"
        assert third_tasks[0].payload == "task4\n"
        assert third_tasks[1].task_id == "line4"
        assert third_tasks[1].payload == "task5\n"
