from config.db import SessionLocal
from queries.CRUD.service import remove_entity, update_entity, list_entities, create_entity
from models import Grade, Student, Subject


def create_grade() -> None:
    print("Enter grade details:")
    print("Available Students:")
    list_entities(Student)
    student_id = input("Enter student ID: ").strip()
    if not student_id or not student_id.isdigit():
        print("Operation canceled.")
        return
    print("Available Subjects:")
    list_entities(Subject)
    subject_id = input("Enter subject ID: ").strip()
    if not student_id or not student_id.isdigit():
        print("Operation canceled.")
        return
    grade = (input("Enter grade: ")).strip()
    if grade == "":
        grade = 0
    elif not grade.isdigit():
        print("Operation canceled.")
        return
    student_id = int(student_id)
    subject_id = int(subject_id)
    grade = int(grade)
    create_entity(Grade, student_id=student_id, subject_id=subject_id, grade=grade)

def list_grades() -> None:
    list_entities(Grade)

def update_grade() -> None:
    grade_id = (input("Enter grade ID to update (or type 'exit' to cancel): ")).strip()
    if grade_id.lower() == "exit" or grade_id == "" or not grade_id.isdigit():
        print("Operation canceled.")
        return
    grade_id = int(grade_id)
    grade_record = SessionLocal().query(Grade).get(grade_id)
    if not grade_record:
        print(f"No grade found with ID {grade_id}.")
        return
    grade = (input("Enter new grade (leave blank to keep current): ")).strip()
    if not grade:
        grade = grade_record.grade
    elif not grade.isdigit():
        print("Operation canceled.")
        return
    update_entity(Grade, grade_id, grade=grade)

def remove_grade() -> None:
    grade_id = (input("Enter grade ID to remove (or type 'exit' to cancel): ")).strip()
    if grade_id.lower() == "exit" or grade_id == "" or not grade_id.isdigit():
        print("Operation canceled.")
        return
    grade_id = int(grade_id)
    grade_record = SessionLocal().query(Grade).get(grade_id)
    if not grade_record:
        print(f"No grade found with ID {grade_id}.")
        return
    remove_entity(Grade, grade_id)
