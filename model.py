from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table


Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class Professor(Base):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    professor_id = Column(Integer, ForeignKey('professors.id'))
    professor = relationship('Professor', back_populates='subjects')

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Float)
    date_received = Column(Date)

    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')

Group.students = relationship('Student', back_populates='group')
Professor.subjects = relationship('Subject', back_populates='professor')
Student.grades = relationship('Grade', back_populates='student')
Subject.grades = relationship('Grade', back_populates='subject')
 
# # Далі потрібно створити об'єкт engine та викликати create_all(), щоб створити таблиці в базі даних
# engine = create_engine('sqlite:///:memory:')
# Base.metadata.create_all(engine)


# # Додайте код для підключення до бази даних SQLite
# engine = create_engine('sqlite:///db1.db')

# # Створіть таблиці у базі даних
# Base.metadata.create_all(engine)
