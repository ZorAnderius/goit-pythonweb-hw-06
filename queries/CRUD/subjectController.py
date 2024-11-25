from config.db import SessionLocal
from queries.CRUD.service import list_entities, create_entity, update_entity, remove_entity
from models import Subject, Teacher

def create_subject() -> None:
    name = (input("Enter subject name (or type 'exit' to cancel): ")).strip()
    if name.lower() == "exit" or name == "":
        print("Operation canceled.")
        return

    print("Available teachers:")
    list_entities(Teacher)
    teacher_id = (input("Enter teacher ID (or type 'exit' to cancel): ")).strip()
    if teacher_id.lower() == "exit" or teacher_id == "" or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)

    create_entity(Subject, name=name, teacher_id=teacher_id)


def list_subjects() -> None:
   list_entities(Subject)


def update_subject() -> None:
    subject_id = (input("Enter subject ID to update (or type 'exit' to cancel): ")).strip()
    if subject_id.lower() == "exit" or subject_id == "" or not subject_id.isdigit():
        print("Operation canceled.")
        return
    subject_id = int(subject_id)
    subject = SessionLocal().query(Subject).get(subject_id)
    if not subject:
        print(f"No subject found with ID {subject_id}.")
        return

    name = (input("Enter new subject name (leave blank to keep current): ")).strip()
    if not name:
        name = subject.name
    else:
        name = name

    print("Available teachers:")
    list_entities(Teacher)
    teacher_id_input = (input("Enter new teacher ID (leave blank to keep current): ")).strip()

    if not teacher_id_input or not teacher_id_input.isdigit():
        teacher_id = subject.teacher_id
    else:
        teacher_id = int(teacher_id_input.strip())
    update_entity(Subject, subject_id, name=name, teacher_id=teacher_id)


def remove_subject() -> None:
    subject_id = (input("Enter subject ID to remove (or type 'exit' to cancel): ")).strip()
    if subject_id.lower() == "exit" or subject_id == "" or not subject_id.isdigit():
        print("Operation canceled.")
        return
    subject_id = int(subject_id)
    student = SessionLocal().query(Subject).get(subject_id)

    if not student:
        print(f"No subject found with ID {subject_id}.")
        return

    remove_entity(Subject, subject_id)
