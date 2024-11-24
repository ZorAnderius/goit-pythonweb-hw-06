from db_queries.CRUD.crud_utils import create_entity, list_entities, update_entity, remove_entity
from models import Teacher


def create_teacher(name):
    name = input("Enter teacher name (or type 'exit' to cancel): ")
    if name.lower() == "exit":
        print("Operation canceled.")
        return
    create_entity(Teacher, name=name)

def list_teachers():
    list_entities(Teacher)

def update_teacher(teacher_id, name):
    teacher_id = int(input("Enter teacher ID to update: "))
    name = input("Enter new teacher name: ")
    update_entity(Teacher, teacher_id, name=name)

def remove_teacher(teacher_id):
    teacher_id = int(input("Enter teacher ID to remove: "))
    remove_entity(Teacher, teacher_id)
