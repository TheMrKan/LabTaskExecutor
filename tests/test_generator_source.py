from unittest.mock import patch

from src.sources.generator_source import GeneratorTaskSource, GeneratedTask

class TestGeneratorTaskSource:
    def test_name(self):
        source = GeneratorTaskSource()
        assert source.name == "random"

    @patch('src.sources.generator_source.random')
    def test_fetch_new_tasks(self, mock_random):
        mock_random.randint.side_effect = [1, 2, 3]
        mock_random.random.side_effect = [0.1, 0.2, 0.3]

        source = GeneratorTaskSource()
        tasks = list(source.fetch_new_tasks())

        assert len(tasks) == 3
        assert all(isinstance(task, GeneratedTask) for task in tasks)

        assert tasks[0].task_id == "1"
        assert tasks[0].payload == 0.1
        assert tasks[1].task_id == "2"
        assert tasks[1].payload == 0.2
        assert tasks[2].task_id == "3"
        assert tasks[2].payload == 0.3
