from rich.console import Console
import sys

from queries.CRUD.gradeController import create_grade, list_grades, update_grade, remove_grade
from queries.CRUD.groupController import create_group, list_groups, update_group, remove_group
from queries.CRUD.studentsController import create_student, list_students, update_student, remove_student
from queries.CRUD.subjectController import create_subject, list_subjects, update_subject, remove_subject
from queries.CRUD.teachersController import create_teacher, list_teachers, update_teacher, remove_teacher
from queries.my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, \
    select_10, select_11, select_12
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
        case "select_1":
            console.print("Select 1: Find 5 students with the highest average grade", style="bold green")
            console.print(select_1())
        case "select_2":
            console.print("Select 2: Find the student with the highest average grade for a specific subject" , style="bold green")
            console.print(select_2())
        case "select_3":
            console.print("Select 3: Find the average grade in groups for a specific subject" , style="bold green")
            console.print(select_3())
        case "select_4":
            console.print("Select 4: Find the average grade across all grades" , style="bold green")
            console.print(select_4())
        case "select_5":
            console.print("Select 5: Find courses taught by a specific teacher" , style="bold green")
            console.print(select_5())
        case "select_6":
            console.print("Select 6: Find the list of students in a specific group" , style="bold green")
            console.print(select_6())
        case "select_7":
            console.print("Select 7: Find grades of students in a specific group for a subject" , style="bold green")
            console.print(select_7())
        case "select_8":
            console.print("Select 8: Find the average grade across all grades" , style="bold green")
            console.print(select_8())
        case "select_9":
            console.print("Select 9: Find the average grade across all grades" , style="bold green")
            console.print(select_9())
        case "select_10":
            console.print("Select 10: Find the average grade across all grades" , style="bold green")
            console.print(select_10())
        case "select_11":
            console.print("Select 11: Find the average grade across all grades" , style="bold green")
            console.print(select_11())
        case "select_12":
            console.print("Select 12: Find the average grade across all grades" , style="bold green")
            console.print(select_12())
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
