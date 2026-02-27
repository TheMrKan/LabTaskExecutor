from unittest.mock import patch

from src.sources.api_source import APITaskSource, APITask

class TestAPITaskSource:
    def test_source_name(self):
        source = APITaskSource("https://api.example.com/tasks")
        assert source.name == "api.example.com"

        source2 = APITaskSource("invalid_url")
        assert source2.name == "invalid_url"

    @patch('src.sources.api_source.json.loads')
    def test_mocked_return(self, mock_json_loads):
        mock_json_loads.return_value = [
            {"task_id": "a", "payload": {}},
            {"task_id": "b", "payload": {}},
            {"task_id": "c", "payload": {}}
        ]

        source = APITaskSource("https://api.example.com/tasks")
        tasks = list(source.fetch_new_tasks())

        assert len(tasks) == 3
        assert all(isinstance(task, APITask) for task in tasks)

        assert tasks[0].task_id == "a"
        assert tasks[0].payload == {}
        assert tasks[1].task_id == "b"
        assert tasks[1].payload == {}
        assert tasks[2].task_id == "c"
        assert tasks[2].payload == {}
