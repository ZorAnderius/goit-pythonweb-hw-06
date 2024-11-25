from typing import List, Tuple, Any
from sqlalchemy import func, desc, Row
from sqlalchemy.orm import Session, InstrumentedAttribute

from models import Student, Grade, Group, Subject
from config.db import session

from queries.CRUD.groupController import list_groups
from queries.CRUD.studentsController import list_students
from queries.CRUD.subjectController import list_subjects
from queries.CRUD.teachersController import list_teachers

def select_1() -> list[Row[tuple[str, Any]]]:
    result = (session.query(Student.name, func.avg(Grade.grade).label('avg_grade'))
            .join(Grade, Student.id == Grade.student_id)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(5)
            .all())
    return result

def select_2() -> Row[tuple[str, Any]] | None:
    list_subjects()
    subject_id = (input("Enter subject id: ")).strip()
    if not subject_id or not subject_id.isdigit():
        print("Operation canceled.")
        return
    subject_id = int(subject_id)

    result = (session.query(Student.name, func.avg(Grade.grade).label('highest_avg_grade'))
            .join(Grade, Student.id == Grade.student_id)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc('highest_avg_grade'))
            .first())
    return result

def select_3() -> list[Row[tuple[int, Any]]] | None:
    list_subjects()
    subject_id = (input("Enter subject id: ")).strip()
    if not subject_id or not subject_id.isdigit():
        print("Operation canceled.")
        return
    subject_id = int(subject_id)

    result = (session.query(
        Group.id.label('group_id'),
        Group.name.label('group_name'),
        func.avg(Grade.grade).label('avg_grade'))
              .join(Student, Group.id == Student.group_id)
              .join(Grade, Student.id == Grade.student_id)
              .filter(Grade.subject_id == subject_id)
              .group_by(Group.id, Group.name)
              .order_by(desc('avg_grade'))
              .all())
    return result


def select_4() -> float:
    result = session.query(func.avg(Grade.grade)).scalar()
    return result

def select_5() -> list[InstrumentedAttribute[str]] | None:
    list_teachers()
    teacher_id = (input("Enter teacher id: ")).strip()
    if not teacher_id or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)

    result = (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return result

def select_6() -> list[InstrumentedAttribute[str]] | None:
    list_groups()
    group_id = (input("Enter teacher id: ")).strip()
    if not group_id or not group_id.isdigit():
        print("Operation canceled.")
        return
    group_id = int(group_id)
    result = (
        session.query(Student.name)
        .filter(Student.group_id == group_id)
        .all()
    )
    return result

def select_7() -> list[Row[tuple[str, Any]]] | None:
    list_groups()
    group_id = (input("Enter group id: ")).strip()
    if not group_id or not group_id.isdigit():
        print("Operation canceled.")
        return
    group_id = int(group_id)

    list_subjects()
    subject_id = (input("Enter subject id: ")).strip()
    if not subject_id or not subject_id.isdigit():
        print("Operation canceled.")
        return
    subject_id = int(subject_id)

    result = (
        session.query(Student.name, Grade.grade)
        .join(Grade, Student.id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return result

def select_8() -> float | None:
    list_teachers()
    teacher_id = (input("Enter teacher id: ")).strip()
    if not teacher_id or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)

    result = (
        session.query(func.avg(Grade.grade).label("average_grade"))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    return result

def select_9() -> list[InstrumentedAttribute[str]] | None:
    list_students()
    student_id = (input("Enter student id: ")).strip()
    if not student_id or not student_id.isdigit():
        print("Operation canceled.")
        return
    student_id = int(student_id)
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    return result

def select_10() -> list[InstrumentedAttribute[str]] | None:
    list_teachers()
    teacher_id = (input("Enter teacher id: ")).strip()
    if not teacher_id or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)

    list_students()
    student_id = (input("Enter student id: ")).strip()
    if not student_id or not student_id.isdigit():
        print("Operation canceled.")
        return
    student_id = int(student_id)

    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .filter(Subject.teacher_id == teacher_id, Grade.student_id == student_id)
        .distinct()
        .all()
    )
    return result

def select_11() -> float | None:
    list_teachers()
    teacher_id = (input("Enter teacher id: ")).strip()
    if not teacher_id or not teacher_id.isdigit():
        print("Operation canceled.")
        return
    teacher_id = int(teacher_id)

    list_students()
    student_id = (input("Enter student id: ")).strip()
    if not student_id or not student_id.isdigit():
        print("Operation canceled.")
        return
    student_id = int(student_id)

    result = (
        session.query(func.avg(Grade.grade).label("average_grade"))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id, Grade.student_id == student_id)
        .scalar()
    )
    return result

def select_12() -> list[Row[tuple[str, Any]]] | None:
    list_groups()
    group_id = (input("Enter teacher id: ")).strip()
    if not group_id or not group_id.isdigit():
        print("Operation canceled.")
        return
    group_id = int(group_id)

    list_subjects()
    subject_id = (input("Enter subject id: ")).strip()
    if not subject_id or not subject_id.isdigit():
        print("Operation canceled.")
        return
    subject_id = int(subject_id)

    subquery = (
        session.query(func.max(Grade.date_received).label("last_lesson"))
        .filter(Grade.subject_id == subject_id)
        .scalar_subquery()
    )

    result = (
        session.query(Student.name, Grade.grade)
        .join(Grade, Student.id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id, Grade.date_received == subquery)
        .all()
    )
    return result