import pytest

from tsusiat.project.task import Task, TaskId
from tsusiat.project.workstream import Workstream


def test_workstream_builds_tasks_by_id():
    a = Task(id=TaskId("A"), title="A")
    b = Task(id=TaskId("B"), title="B")
    ws = Workstream([a, b])

    assert ws.get_task(TaskId("A")) is a
    assert ws.get_task(TaskId("B")) is b


def test_workstream_includes_subtasks_in_index():
    sub = Task(id=TaskId("A-1"), title="A-1")
    a = Task(id=TaskId("A"), title="A", subtasks=[sub])

    ws = Workstream([a])

    assert ws.get_task(TaskId("A")) is a
    assert ws.get_task(TaskId("A-1")) is sub


def test_workstream_get_task_not_found_raises_exception():
    a = Task(id=TaskId("A"), title="A")
    ws = Workstream([a])

    with pytest.raises(KeyError, match="not found"):
        ws.get_task(TaskId("B"))


def test_workstream_rejects_duplicate_task_ids():
    a1 = Task(id=TaskId("A"), title="A1")
    a2 = Task(id=TaskId("A"), title="A2")

    with pytest.raises(ValueError, match="Duplicate task"):
        Workstream([a1, a2])
