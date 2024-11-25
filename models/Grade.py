from sqlalchemy import Integer, ForeignKey, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from .Base import Base

class Grade(Base):
    __tablename__ = 'grades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey('subjects.id'), nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=True)
    date_received: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    student: Mapped['Student'] = relationship('Student', back_populates='grades')
    subject: Mapped['Subject'] = relationship('Subject', back_populates='grades')