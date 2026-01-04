from datetime import date

from tsusiat.project.task import Task, TaskId
from tsusiat.project.workstream import Workstream


def large_project_tasks() -> Workstream:
    one_day_effort = 6
    two_days_effort = 12
    three_days_effort = 18
    five_days_effort = 30
    in_eight_months = date(2024, 6, 1)

    dev_epic_id = TaskId("TASK-001")
    development_epic = Task(
        id=dev_epic_id,
        title="[Task Manager] Development Phase",
        subtasks=[
            Task(
                id=TaskId(f"{dev_epic_id}A"),
                title="[Task Manager] High Level Design",
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}B"),
                title="[Task Manager] Low Level Design",
                dependencies=[TaskId("TASK-001A")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}C"),
                title="Create Task table in data store",
                dependencies=[TaskId(f"{dev_epic_id}B")],
                estimated_effort_hours=two_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}D"),
                title="Implement CreateTask API",
                dependencies=[TaskId(f"{dev_epic_id}C")],
                estimated_effort_hours=three_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}E"),
                title="Implement UpdateTask API",
                dependencies=[TaskId(f"{dev_epic_id}D")],
                estimated_effort_hours=three_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}F"),
                title="Implement DeleteTask API",
                dependencies=[TaskId(f"{dev_epic_id}E")],
                estimated_effort_hours=three_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}G"),
                title="Implement SearchTasks API",
                dependencies=[TaskId(f"{dev_epic_id}F")],
                estimated_effort_hours=three_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}H"),
                title="[Task Manager] Low Level Design Refresh",
                dependencies=[TaskId(f"{dev_epic_id}B")],
                estimated_effort_hours=two_days_effort,
            ),
            Task(
                id=TaskId(f"{dev_epic_id}Z"),
                title="[Task Manager] Scope Increase Buffer",
                dependencies=[TaskId(f"{dev_epic_id}H")],
                estimated_effort_hours=five_days_effort * 2,
            ),
        ],
    )

    e2e_epic_id = TaskId("TASK-002")
    end_to_end_testing_epic = Task(
        id=e2e_epic_id,
        title="[Task Manager] End-to-End Tests",
        subtasks=[
            Task(
                id=TaskId(f"{e2e_epic_id}A"),
                title="Create Task Management E2E Test for CreateTask API",
                dependencies=[TaskId(f"{dev_epic_id}D")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{e2e_epic_id}B"),
                title="Expand Task Management E2E Test with UpdateTask API",
                dependencies=[TaskId(f"{dev_epic_id}E")],
                estimated_effort_hours=two_days_effort,
            ),
            Task(
                id=TaskId(f"{e2e_epic_id}C"),
                title="Expand Task Management E2E Test with DeleteTask API",
                dependencies=[TaskId(f"{dev_epic_id}F")],
                estimated_effort_hours=two_days_effort,
            ),
            Task(
                id=TaskId(f"{e2e_epic_id}D"),
                title="Expand Task Management E2E Test with SearchTasks API",
                dependencies=[TaskId(f"{dev_epic_id}G")],
                estimated_effort_hours=two_days_effort,
            ),
        ],
    )

    sec_epic_id = TaskId("TASK-003")
    security_review_epic = Task(
        id=sec_epic_id,
        title="[Task Manager] Security Review",
        subtasks=[
            Task(
                id=TaskId(f"{sec_epic_id}A"),
                title="[Task Manager] Threat Model Document",
                dependencies=[TaskId(f"{dev_epic_id}H")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{sec_epic_id}B"),
                title="[Task Manager] Pentest Scope Document",
                dependencies=[TaskId(f"{sec_epic_id}A")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{sec_epic_id}C"),
                title="[Task Manager] Security Audit Queue",
                dependencies=[TaskId(f"{sec_epic_id}B")],
                fixed_duration_days=3 * 30,
            ),
            Task(
                id=TaskId(f"{sec_epic_id}D"),
                title="[Task Manager] Pentest Execution Support",
                dependencies=[TaskId(f"{sec_epic_id}C")],
                estimated_effort_hours=two_days_effort,
            ),
            Task(
                id=TaskId(f"{sec_epic_id}Z"),
                title="[Task Manager] Finding Fixes & Retest Buffer",
                dependencies=[TaskId(f"{sec_epic_id}D")],
                estimated_effort_hours=five_days_effort * 2,
            ),
        ],
    )

    qa_epic_id = TaskId("TASK-004")
    quality_assurance_epic = Task(
        id=qa_epic_id,
        title="[Task Manager] Quality Assurance",
        subtasks=[
            Task(
                id=TaskId(f"{qa_epic_id}A"),
                title="[Task Manager] Manual Validation Design & Plan Document",
                dependencies=[TaskId(f"{dev_epic_id}H")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{qa_epic_id}B"),
                title="[Task Manager] Manual Validation Environment & Tooling Setup",
                dependencies=[TaskId(f"{qa_epic_id}A"), dev_epic_id],
                estimated_effort_hours=three_days_effort,
            ),
            Task(
                id=TaskId(f"{qa_epic_id}C"),
                title="[Task Manager] Manual Validation Execution",
                dependencies=[TaskId(f"{qa_epic_id}B")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{qa_epic_id}D"),
                title="[Task Manager] Bug Fixes & Exercise Repeat Buffer",
                dependencies=[TaskId(f"{qa_epic_id}C")],
                estimated_effort_hours=five_days_effort * 2,
            ),
        ],
    )

    load_epic_id = TaskId("TASK-006")
    load_testing_epic = Task(
        id=load_epic_id,
        title="[Task Manager] Load Testing",
        subtasks=[
            Task(
                id=TaskId(f"{load_epic_id}A"),
                title="[Task Manager] Load Test Plan Document",
            ),
            Task(
                id=TaskId(f"{load_epic_id}B"),
                title="[Task Manager] Load Test Environment & Tooling Setup",
                dependencies=[TaskId(f"{load_epic_id}A")],
            ),
            Task(
                id=TaskId(f"{load_epic_id}C"),
                title="[Task Manager] Load Test Execution",
                dependencies=[TaskId(f"{load_epic_id}B")],
            ),
            Task(
                id=TaskId(f"{load_epic_id}D"),
                title="[Task Manager] Performance Fixes & Exercise Repeat Buffer",
                dependencies=[TaskId(f"{load_epic_id}C")],
                estimated_effort_hours=five_days_effort * 2,
            ),
        ],
    )

    chaos_epic_id = TaskId("TASK-007")
    chaos_testing_epic = Task(
        id=chaos_epic_id,
        title="[Task Manager] Chaos Testing",
        subtasks=[
            Task(
                id=TaskId(f"{chaos_epic_id}A"),
                title="[Task Manager] Chaos Test Plan Document",
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{chaos_epic_id}B"),
                title="[Task Manager] Chaos Test Environment & Tooling Setup",
                dependencies=[TaskId(f"{chaos_epic_id}A")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{chaos_epic_id}C"),
                title="[Task Manager] Chaos Test Execution",
                dependencies=[TaskId(f"{chaos_epic_id}B")],
                estimated_effort_hours=five_days_effort,
            ),
            Task(
                id=TaskId(f"{chaos_epic_id}D"),
                title="[Task Manager] Monitoring Fixes & Exercise Repeat Buffer",
                dependencies=[TaskId(f"{chaos_epic_id}C")],
                estimated_effort_hours=five_days_effort * 2,
            ),
        ],
    )

    compliance_epic_id = TaskId("TASK-008")
    compliance_review_epic = Task(
        id=compliance_epic_id,
        title="[Task Manager] Compliance Review",
        subtasks=[],
    )

    launch_epic_id = TaskId("TASK-009")
    launch_epic = Task(
        id=launch_epic_id,
        title="[Task Manager] Deployment",
        subtasks=[
            Task(
                id=TaskId(f"{launch_epic_id}A"),
                title="[Task Manager] Allowlist customer previews",
                dependencies=[
                    sec_epic_id,
                    qa_epic_id,
                    load_epic_id,
                    chaos_epic_id,
                    compliance_epic_id,
                ],
                estimated_effort_hours=one_day_effort,
            ),
            Task(
                id=TaskId(f"{launch_epic_id}B"),
                title="[Task Manager] Remove allowlist feature toggles",
                dependencies=[TaskId(f"{launch_epic_id}A")],
                estimated_effort_hours=one_day_effort,
                goal_date=in_eight_months,
            ),
        ],
    )

    follow_up_epic_id = TaskId("TASK-010")
    follow_up_epic = Task(
        id=follow_up_epic_id,
        title="[Task Manager] Post-Launch Follow-Up",
        subtasks=[
            Task(
                id=TaskId(f"{follow_up_epic_id}A"),
                title="[Task Manager] Post-Launch Monitoring & Bug Fixes",
                dependencies=[TaskId(f"{launch_epic_id}B")],
                estimated_effort_hours=five_days_effort * 2,
            ),
            Task(
                id=TaskId(f"{follow_up_epic_id}B"),
                title="[Task Manager] Customer Feedback Collection & Analysis",
                dependencies=[TaskId(f"{follow_up_epic_id}A")],
                estimated_effort_hours=five_days_effort * 2,
            ),
        ],
    )

    project_goal_id = TaskId("PROJECT-001")
    project_goal = Task(
        id=project_goal_id,
        title="Task Manager Feature Complete",
        subtasks=[
            development_epic,
            end_to_end_testing_epic,
            security_review_epic,
            quality_assurance_epic,
            load_testing_epic,
            chaos_testing_epic,
            compliance_review_epic,
            launch_epic,
        ],
    )

    return Workstream([project_goal, follow_up_epic])
