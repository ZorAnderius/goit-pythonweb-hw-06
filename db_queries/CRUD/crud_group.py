from db_queries.CRUD.crud_utils import create_entity, list_entities, update_entity, remove_entity
from models import Group

def create_group():
    name = input("Enter group name (or type 'exit' to cancel): ")
    if name.lower() == "exit":
        print("Operation canceled.")
        return
    create_entity(Group, name=name)

def list_groups():
    list_entities(Group)

def update_group():
    group_id = int(input("Enter group ID to update: "))
    name = input("Enter new group name: ")
    update_entity(Group, group_id, name=name)

def remove_group():
    group_id = int(input("Enter group ID to remove: "))
    remove_entity(Group, group_id)
