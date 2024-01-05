from connect_db import session

from faker import Faker
from datetime import datetime, timedelta
from model import Base, Group, Professor, Student, Subject, Grade

# Ініціалізація генератора випадкових даних
fake = Faker()

# Створення груп
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів
professors = [Professor(name=fake.name()) for _ in range(5)]
session.add_all(professors)
session.commit()

# Створення предметів і прив'язка їх до викладачів
subjects = [Subject(name=fake.word(), professor_id=professor.id) for professor in professors for _ in range(2)]
session.add_all(subjects)
session.commit()

# Створення студентів та прив'язка їх до груп
students = [Student(name=fake.name(), group_id=fake.random_element(elements=[group.id for group in groups])) for _ in range(30)]
session.add_all(students)
session.commit()

# Створення оцінок для студентів з усіх предметів
for student in students:
    for subject in subjects:
        grade = Grade(
            student_id=student.id,
            subject_id=subject.id,
            grade=fake.random_element(elements=[3.0, 3.5, 4.0, 4.5, 5.0]),
            date_received=fake.date_between(start_date='-30d', end_date='today')
        )
        session.add(grade)

session.commit()

print("Базу даних успішно заповнено випадковими даними.")
