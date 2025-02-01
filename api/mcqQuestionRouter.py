from fastapi import APIRouter, status
from services.mcqQuestionService import get_all_mcq_questions,Create_mcq_question,get_one_mcq_question,update_mcq_question,delete_mcq_question
from schemas.mcqSchema import mcqSchema

router = APIRouter(
    prefix="/mcqquestion",
    tags=[" mcqquestions"]
)

@router.get("/" ,status_code=status.HTTP_200_OK, response_model=list[mcqSchema])
def get_all():
    return get_all_mcq_questions()


@router.post("/" ,status_code=status.HTTP_200_OK)
def create_mcq_question(mcqSchema: mcqSchema):
    return Create_mcq_question(mcqSchema)

@router.get("/{id}" ,status_code=status.HTTP_200_OK)
def get_one(id: str):
    return get_one_mcq_question(id)

@router.put("/{id}" ,status_code=status.HTTP_200_OK)
def update_one(id: str, mcqSchema: mcqSchema):
    return update_mcq_question(id, mcqSchema)

@router.delete("/{id}" ,status_code=status.HTTP_200_OK)
def delete_one(id: str):
    return delete_mcq_question(id)