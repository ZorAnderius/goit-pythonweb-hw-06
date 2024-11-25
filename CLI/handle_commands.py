from rich.console import Console
import sys

from queries.CRUD.gradeController import create_grade, list_grades, update_grade, remove_grade
from queries.CRUD.groupController import create_group, list_groups, update_group, remove_group
from queries.CRUD.studentsController import create_student, list_students, update_student, remove_student
from queries.CRUD.subjectController import create_subject, list_subjects, update_subject, remove_subject
from queries.CRUD.teachersController import create_teacher, list_teachers, update_teacher, remove_teacher
from queries.seed import seed_teachers, seed_groups, seed_subjects, seed_students, seed_grades
from utils.clean_all_tables import clean_all_tables
from utils.command_help import command_help
from utils.seed_tables import seed_tables

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
        case "create-subject":
            create_subject()
        case "list-subjects":
            list_subjects()
        case "update-subject":
            update_subject()
        case "delete-subject":
            remove_subject()
        case "help":
            command_help()
        case "seed-data":
            seed_tables()
        case "clean-all-tables":
            clean_all_tables()
        case command if command in ["exit", "close"]:
            console.print("Goodbye!", style="bold blue")
            sys.exit(0)
        case _:
            console.print(f"Unknown command: {command}", style="bold red")
