from db_queries.CRUD.crud_utils import remove_entity, update_entity, list_entities, create_entity
from models import Grade

def create_grade():
    student_id = int(input("Enter student ID: "))
    subject_id = int(input("Enter subject ID: "))
    grade = int(input("Enter grade: "))
    create_entity(Grade, student_id=student_id, subject_id=subject_id, grade=grade)

def list_grades():
    list_entities(Grade)

def update_grade():
    grade_id = int(input("Enter grade ID to update: "))
    grade = int(input("Enter new grade: "))
    update_entity(Grade, grade_id, grade=grade)

def remove_grade():
    grade_id = int(input("Enter grade ID to remove: "))
    remove_entity(Grade, grade_id)
