from queries.CRUD.service import remove_all_entities
from models import Grade, Student, Subject, Teacher, Group


def clean_all_tables() -> None:
    remove_all_entities(Grade)
    remove_all_entities(Student)
    remove_all_entities(Subject)
    remove_all_entities(Teacher)
    remove_all_entities(Group)