from fastapi import APIRouter, status
from services.ai_services import get_explaination , get_report
from schemas.aiSchema import WrongAnswerSchema , ReportSchema
router = APIRouter(
    prefix="/ai",
    tags=["ai"]
)

@router.post("/explain" ,status_code=status.HTTP_200_OK)
def explain_wrong_answer(wrong_answer: WrongAnswerSchema):
    return get_explaination(wrong_answer)

@router.get("/report" ,status_code=status.HTTP_200_OK , description="Api under development")
def get_report_quiz(question: str):
    return get_report(question)
