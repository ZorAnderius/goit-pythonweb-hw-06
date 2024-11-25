from queries.seed import seed_groups, seed_teachers, seed_subjects, seed_students, seed_grades


def seed_tables() -> None:
    print("Seeding database...")
    groups = seed_groups()
    print(f"Created {len(groups)} groups.")
    teachers = seed_teachers()
    print(f"Created {len(teachers)} teachers.")
    subjects = seed_subjects(teachers)
    print(f"Created {len(subjects)} subjects.")
    students = seed_students(groups)
    print(f"Created {len(students)} students.")
    seed_grades(students, subjects)
    print("Grades have been added.")
    print("Seeding complete!")