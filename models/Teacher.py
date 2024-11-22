from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    subjects: Mapped[list['Subject']] = relationship('Subject', back_populates='teacher')