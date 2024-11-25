from rich.console import Console

console = Console()

def command_help() -> None:
    console.print("Available commands:", style="bold green")
    commands = [
        ("create-teacher", "Create a new teacher."),
        ("list-teachers", "List all teachers."),
        ("update-teacher", "Update an existing teacher."),
        ("delete-teacher", "Delete a teacher by ID."),
        ("create-student", "Create a new student."),
        ("list-students", "List all students."),
        ("update-student", "Update an existing student."),
        ("delete-student", "Delete a student by ID."),
        ("create-group", "Create a new group."),
        ("list-groups", "List all groups."),
        ("update-group", "Update an existing group."),
        ("delete-group", "Delete a group by ID."),
        ("create-grade", "Create a new grade."),
        ("list-grades", "List all grades."),
        ("update-grade", "Update an existing grade."),
        ("delete-grade", "Delete a grade by ID."),
        ("create-subject", "Create a new subject."),
        ("list-subjects", "List all subjects."),
        ("update-subject", "Update an existing subject."),
        ("delete-subject", "Delete a subject by ID."),
        ("select_1", "Find 5 students with the highest average grade"),
        ("select_2", "Find the student with the highest average grade for a specific subject"),
        ("select_3", "Find the average grade in groups for a specific subject"),
        ("select_4", "Find the average grade across all grades"),
        ("select_5", "Find courses taught by a specific teacher"),
        ("select_6", "Find the list of students in a specific group"),
        ("select_7", "Find grades of students in a specific group for a subject"),
        ("select_8", "Find the average grade given by a specific teacher for their subjects"),
        ("select_9", "Find courses attended by a specific student"),
        ("select_10", "Find courses taught by a specific teacher to a specific student"),
        ("select_11", "Find the average grade given by a specific teacher to a specific student"),
        ("select_12", "Find grades for students in a specific group for a subject during the last lesson"),
        ("seed-data", "Seed the database with random data."),
        ("clean-all-tables", "Clean all tables in the database."),
        ("help", "Show a help message."),
        ("exit", "Exit the program."),
    ]
    for cmd, desc in commands:
        console.print(f"[bold green]{cmd:20}[/bold green] - [white]{desc}[/white]")