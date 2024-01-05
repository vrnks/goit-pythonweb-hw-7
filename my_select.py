from sqlalchemy import create_engine, func, desc
from connect_db import session
from model import Group, Professor, Student, Subject, Grade


# Запит 1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    query = (
        session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(5)
    )
    return query.all()

# Запит 2: Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject_name):
    query = (
        session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(1)
    )
    return query.first()

# Запит 3: Знайти середній бал у групах з певного предмета.
def select_3(subject_name):
    query = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Student, Group.id == Student.group_id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == subject_name) \
        .group_by(Group.id)

    return query.all()

# Запит 4: Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    query = (
        session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))
    )
    return query.first()
    

# Запит 5: Знайти які курси читає певний викладач.
def select_5(professor_name):
    query = (
        session.query(Subject.name)
        .join(Professor)
        .filter(Professor.name == professor_name)
    )
    return query.all()

# Запит 6: Знайти список студентів у певній групі.
def select_6(group_name):
    query = (
        session.query(Student.name)
        .join(Group)
        .filter(Group.name == group_name)
    )
    return query.all()

# Запит 7: Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(group_name, subject_name):
    query = (
        session.query(Student.name, Grade.grade)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
    )
    return query.all()

# Запит 8: Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(professor_name):
    query = (
        session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .join(Subject)
        .join(Professor)
        .filter(Professor.name == professor_name)
        .scalar()
    )
    return query

# Запит 9: Знайти список курсів, які відвідує певний студент.
def select_9(student_name):
    query = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .filter(Student.name == student_name)
        .all()
    )
    return query

# Запит 10: Список курсів, які певному студенту читає певний викладач.
def select_10(student_name, professor_name):
    query = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .join(Professor)
        .filter(Student.name == student_name, Professor.name == professor_name)
        .all()
    )
    return query

if __name__ == "__main__":
    result = select_1()
    print("Запит 1:")
    print(result)
    
    result = select_2('risk')
    print("Запит 2:")
    print(result)
    
    result = select_3('risk')
    print("Запит 3:")
    print(result)
    
    result = select_4()
    print("Запит 4:")
    print(result)
    
    result = select_5('Katrina Weaver')
    print("Запит 5:")
    print(result)
    
    result = select_6('specific')
    print("Запит 6:")
    print(result)
    
    result = select_7('specific', 'risk')
    print("Запит 7:")
    print(result)
    
    result = select_8('Katrina Weaver')
    print("Запит 8:")
    print(result)
    
    result = select_9('Amanda Phillips')
    print("Запит 9:")
    print(result)
    
    result = select_10('Amanda Phillips', 'Katrina Weaver')
    print("Запит 10:")
    print(result)
    
# Запит 1:
# [('Warren Gonzalez', 4.35), ('Teresa Torres', 4.25), ('Angela Anderson', 4.25), ('Doris Garcia', 4.2), ('Paul Hatfield', 4.2)]
# Запит 2:
# ('Christina Davis', 5.0)
# Запит 3:
# [('specific', 4.4), ('once', 4.12), ('media', 4.04)]
# Запит 4:
# (4.02,)
# Запит 5:
# [('like',), ('yes',)]
# Запит 6:
# [('Amanda Phillips',), ('Francisco Perry',), ('Teresa Torres',), ('Kathy Neal',), ('Christina Davis',)]
# Запит 7:
# [('Amanda Phillips', 3.0), ('Francisco Perry', 4.0), ('Teresa Torres', 5.0), ('Kathy Neal', 5.0), ('Christina Davis', 5.0)]
# Запит 8:
# 4.05
# Запит 9:
# [('like',), ('yes',), ('rest',), ('between',), ('collection',), ('yeah',), ('risk',), ('perform',), ('there',), ('strategy',)]
# Запит 10:
# [('like',), ('yes',)]   
