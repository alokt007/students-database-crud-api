from app.database import get_db
from app.models import Student
from app.schemas import StudentCreate, StudentResponse
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/students", tags=["Students"])

 
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
  db_student = Student(**student.model_dump())
  db.add(db_student)
  db.commit()
  db.refresh(db_student)
  return db_student