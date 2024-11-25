from config.db import session
from queries.CRUD.service import create_entity, list_entities, update_entity, remove_entity
from models import Group

def create_group() -> None:
    name = (input("Enter group name (or type 'exit' to cancel): ")).strip()
    if name.lower() == "exit" or name == "":
        print("Operation canceled.")
        return
    create_entity(Group, name=name)

def list_groups() -> None:
    list_entities(Group)

def update_group() -> None:
    group_id = (input("Enter group ID to update (or type 'exit' to cancel): ")).strip()
    if group_id.lower() == "exit" or group_id == "" or not group_id.isdigit():
        print("Operation canceled.")
        return
    group_id = int(group_id)
    group = session.query(Group).get(group_id)

    if not group:
        print(f"No group found with ID {group_id}.")
        return

    name = (input("Enter new group name: ")).strip()
    if not name:
        name = group.name
    else:
        name = name
    update_entity(Group, int(group_id), name=name)

def remove_group() -> None:
    group_id = (input("Enter group ID to update (or type 'exit' to cancel): ")).strip()
    if group_id.lower() == "exit" or group_id== "" or not group_id.isdigit():
        print("Operation canceled.")
        return
    group_id = int(group_id)
    group = session.query(Group).get(group_id)

    if not group:
        print(f"No group found with ID {group_id}.")
        return

    remove_entity(Group,int(group_id))
