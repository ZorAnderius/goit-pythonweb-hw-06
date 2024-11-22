from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey('teachers.id'), nullable=False)

    teacher: Mapped['Teacher'] = relationship('Teacher', back_populates='subjects')
    grades: Mapped[list['Grade']] = relationship('Grade', back_populates='subject')