from config.db import SessionLocal
from queries.CRUD.service import create_entity, list_entities, update_entity, remove_entity
from models import Teacher


def create_teacher() -> None:
    name = (input("Enter teacher name (or type 'exit' to cancel): ")).strip()
    if name.lower() == "exit" or name == "":
        print("Operation canceled.")
        return
    create_entity(Teacher, name=name)

def list_teachers() -> None:
    list_entities(Teacher)

def update_teacher() -> None:
    teacher_id = (input("Enter teacher ID to update (or type 'exit' to cancel): ")).strip()
    if teacher_id.lower() == "exit" or teacher_id == "" or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)
    teacher = SessionLocal().query(Teacher).get(teacher_id)

    if not teacher:
        print(f"No teacher found with ID {teacher_id}.")
        return
    name = (input("Enter new teacher name: ")).strip()
    if not name:
        name = teacher.name
    else:
        name = name.strip()
    update_entity(Teacher, teacher_id, name=name)

def remove_teacher() -> None:
    teacher_id = (input("Enter teacher ID to remove (or type 'exit' to cancel): ")).strip()
    if teacher_id.lower() == "exit" or teacher_id== "" or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)
    student = SessionLocal().query(Teacher).get(teacher_id)

    if not student:
        print(f"No teacher found with ID {teacher_id}.")
        return
    remove_entity(Teacher, teacher_id)
