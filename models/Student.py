from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey('groups.id'), nullable=False)

    group: Mapped['Group'] = relationship('Group', back_populates='students')
    grades: Mapped[list['Grade']] = relationship('Grade', back_populates='student')