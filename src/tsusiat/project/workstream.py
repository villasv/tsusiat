from tsusiat.project.task import Task, TaskId


class Workstream:
    def __init__(self, tasks: list[Task]) -> None:
        self._tasks = tasks

        self._tasks_by_id: dict[TaskId, Task] = {}
        for task in self._traverse_depth_first(tasks):
            if task.id in self._tasks_by_id:
                raise ValueError(f"Duplicate task {task.id}")
            self._tasks_by_id[task.id] = task

    def get_task(self, task_id: TaskId) -> Task:
        if task := self._tasks_by_id.get(task_id):
            return task
        raise KeyError(f"Task {task_id} not found")

    @staticmethod
    def _traverse_depth_first(tasks: list[Task]):
        for task in tasks:
            yield task
            yield from Workstream._traverse_depth_first(task.subtasks)
