from rich.console import Console
import sys

from db_queries.CRUD.crud_grade import create_grade, list_grades, update_grade, remove_grade
from db_queries.CRUD.crud_group import create_group, list_groups, update_group, remove_group
from db_queries.CRUD.crud_students import create_student, list_students, update_student, remove_student
from db_queries.CRUD.crud_teachers import create_teacher, list_teachers, update_teacher, remove_teacher

console = Console()

def handle_command(command, args):
    match command:
        case "create-teacher":
            create_teacher()
        case "list-teachers":
            list_teachers()
        case "update-teacher":
            update_teacher()
        case "delete-teacher":
            remove_teacher()
        case "create-student":
            create_student()
        case "list-students":
            list_students()
        case "update-student":
            update_student()
        case "delete-student":
            remove_student()
        case "create-group":
            create_group()
        case "list-groups":
            list_groups()
        case "update-group":
            update_group()
        case "delete-group":
            remove_group()
        case "create-grade":
            create_grade()
        case "list-grades":
            list_grades()
        case "update-grade":
            update_grade()
        case "delete-grade":
            remove_grade()
        case command if command in ["exit", "close"]:
            console.print("Goodbye!", style="bold blue")
            sys.exit(0)
        case _:
            console.print(f"Unknown command: {command}", style="bold red")
