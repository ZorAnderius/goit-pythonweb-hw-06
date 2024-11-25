from config.db import SessionLocal
from queries.CRUD.groupController import list_groups
from queries.CRUD.service import create_entity, list_entities, update_entity, remove_entity, session
from models import Student

def create_student() -> None:
    name = (input("Enter student name (or type 'exit' to cancel): ")).strip()
    if name.lower() == "exit" or name == "":
        print("Operation canceled.")
        return

    print("Available Groups:")
    list_groups()
    group_id = (input("Enter group ID (or type 'exit' to cancel): ")).strip()
    if group_id.lower() == 'exit' or group_id == '' or not group_id.isdigit():
        print("Operation canceled.")
        return
    group_id = int(group_id)
    create_entity(Student, name=name, group_id=group_id)

def list_students():
    list_entities(Student)

def update_student() -> None:
    student_id = (input("Enter student ID to update (or type 'exit' to cancel): ")).strip()
    if student_id.lower() == "exit" or student_id == "" or not student_id.isdigit():
        print("Operation canceled.")
        return
    student_id = int(student_id)
    student = SessionLocal().query(Student).get(student_id)

    if not student:
        print(f"No student found with ID {student_id}.")
        return

    name = (input("Enter new student name: ")).strip()
    if not name:
        name = student.name
    else:
        name = name

    print("Available Groups:")
    list_groups()
    group_id_input = (input("Enter new group ID: ")).strip()
    if not group_id_input or not group_id_input.isdigit():
        group_id = student.group_id
    else:
        group_id = int(group_id_input)
    update_entity(Student, int(student_id), name=name, group_id=group_id)

def remove_student() -> None:
    student_id = (input("Enter student ID to remove (or type 'exit' to cancel): ")).strip()
    if student_id.lower() == "exit" or student_id == "" or not student_id.isdigit():
        print("Operation canceled.")
        return
    student_id = int(student_id)
    student = SessionLocal().query(Student).get(student_id)

    if not student:
        print(f"No student found with ID {student_id}.")
        return
    remove_entity(Student, student_id)
