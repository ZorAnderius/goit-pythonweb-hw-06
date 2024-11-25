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
        ("help", "Show a help message."),
        ("seed-data", "Seed the database with random data."),
        ("clean-all-tables", "Clean all tables in the database."),
        ("exit", "Exit the program."),
    ]
    for cmd, desc in commands:
        console.print(f"[bold green]{cmd:20}[/bold green] - [white]{desc}[/white]")