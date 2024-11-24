from typing import Type, Any, Dict
from sqlalchemy.ext.declarative import as_declarative
from config.db import SessionLocal

session = SessionLocal()

def create_entity(entity_class: Type[as_declarative], **kwargs: Any) -> None:
    entity = entity_class(**kwargs)
    session.add(entity)
    session.commit()
    print(f"{entity_class.__name__} '{kwargs}' created successfully.")

def list_entities(entity_class: Type[as_declarative]) -> None:
    entities = session.query(entity_class).all()
    for entity in entities:
        print(f"ID: {entity.id}, Attributes: {entity.__dict__}")

def update_entity(entity_class: Type[as_declarative], entity_id: int, **kwargs: Any) -> None:
    entity = session.query(entity_class).get(entity_id)
    if not entity:
        print(f"No {entity_class.__name__} found with ID {entity_id}.")
        return
    for key, value in kwargs.items():
        setattr(entity, key, value)
    session.commit()
    print(f"{entity_class.__name__} with ID {entity_id} updated to {kwargs}.")

def remove_entity(entity_class: Type[as_declarative], entity_id: int) -> None:
    entity = session.query(entity_class).get(entity_id)
    if not entity:
        print(f"No {entity_class.__name__} found with ID {entity_id}.")
        return
    session.delete(entity)
    session.commit()
    print(f"{entity_class.__name__} with ID {entity_id} removed successfully.")
