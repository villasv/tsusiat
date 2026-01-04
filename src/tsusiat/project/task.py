from datetime import date, datetime
from typing import NewType

TaskId = NewType("TaskId", str)


class Task:
    def __init__(
        self,
        *,
        id: TaskId,
        title: str,
        # Scoping fields
        subtasks: list[Task] | None = None,
        dependencies: list[TaskId] | None = None,
        # Timing fields
        fixed_duration_days: int | None = None,
        estimated_effort_hours: int | None = None,
        # Target
        goal_date: date | None = None,  # individual task own target, usually milestones
        need_by_date: date | None = None,  # derive from dependency goal / need by dates
        # Timing fields
        projected_initiation_datetime: datetime | None = None,
        projected_completion_datetime: datetime | None = None,
    ) -> None:
        self.id = id
        self.title = title
        self.subtasks = subtasks or []
        self.dependencies = dependencies or []

        if estimated_effort_hours and estimated_effort_hours < 0:
            raise ValueError("Estimated effort hours must be positive if set")
        if fixed_duration_days and fixed_duration_days < 0:
            raise ValueError("Fixed duration days must be positive if set")
        if estimated_effort_hours is not None and fixed_duration_days is not None:
            raise ValueError("Task cannot specify both effort hours and duration days")

        self.fixed_duration_days = fixed_duration_days
        self.estimated_effort_hours = estimated_effort_hours

        self.goal_date = goal_date
        self.need_by_date = need_by_date

        if projected_initiation_datetime and projected_completion_datetime:
            if projected_completion_datetime < projected_initiation_datetime:
                raise ValueError("Projected completion cannot be before initiation")

        self.projected_initiation_datetime = projected_initiation_datetime
        self.projected_completion_datetime = projected_completion_datetime
