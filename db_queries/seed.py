from faker import Faker
import random

from config.db import SessionLocal
from models import Group, Teacher, Subject, Student, Grade

session = SessionLocal()
fake = Faker()

def seed_groups():
    groups = [Group(name=f'Group {i}') for i in range(1, 4)]
    session.add_all(groups)
    session.commit()
    return groups

def seed_teachers():
    teachers = [Teacher(name=fake.name()) for _ in range(random.randint(2, 5))]
    session.add_all(teachers)
    session.commit()
    return teachers

def seed_subjects(teachers):
    subjects = [Subject(name=fake.job(), teacher=random.choice(teachers)) for _ in range(random.randint(5, 8))]
    session.add_all(subjects)
    session.commit()
    return subjects

def seed_students( groups):
    students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(random.randint(30, 50))]
    session.add_all(students)
    session.commit()
    return students

def seed_grades(students, subjects):
    grades = []
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(15, 20)):
                grades.append(
                    Grade(
                        grade=random.randint(1, 100),
                        student=student,
                        subject=subject,
                    )
                )
    session.add_all(grades)
    session.commit()
    return grades