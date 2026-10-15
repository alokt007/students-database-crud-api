from app.database import Base
from sqlalchemy import Column, Date, Integer, String

 
class Student(Base):
  __tablename__ = "students"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  student_name = Column(String, index=True, nullable=False)
  student_class = Column(String, nullable=False)
  student_section = Column(String, nullable=False)
  student_dob = Column(Date, nullable=False)
  student_email = Column(String, nullable=False)
  student_sub = Column(String)