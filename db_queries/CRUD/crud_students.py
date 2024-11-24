from config.db import SessionLocal
from db_queries.CRUD.crud_group import list_groups
from db_queries.CRUD.crud_utils import create_entity, list_entities, update_entity, remove_entity, session
from models import Student

def create_student():
    name = input("Enter student name (or type 'exit' to cancel): ")
    if name.lower() == "exit":
        print("Operation canceled.")
        return
    print("Available Groups:")
    list_groups()
    group_id = input("Enter group ID (or type 'exit' to cancel): ")
    if group_id.lower() == 'exit':
        print("Operation canceled.")
        return
    try:
        group_id = int(group_id)
    except ValueError:
        print("Invalid input. Please enter a valid group ID.")
        return
    create_entity(Student, name=name, group_id=group_id)

def list_students():
    list_entities(Student)

def update_student():
    student_id = int(input("Enter student ID to update: "))
    student = SessionLocal().query(Student).get(student_id)

    if not student:
        print(f"No student found with ID {student_id}.")
        return
    name = input("Enter new student name: ")
    if not name:
        name = student.name
    print("Available Groups:")
    list_groups()
    group_id_input = int(input("Enter new group ID: "))
    if not group_id_input:
        group_id = student.group_id
    else:
        try:
            group_id = int(group_id_input)
        except ValueError:
            print("Invalid group ID. Operation canceled.")
            return
    update_entity(Student, student_id, name=name, group_id=group_id)

def remove_student():
    student_id = int(input("Enter student ID to remove: "))
    remove_entity(Student, student_id)
