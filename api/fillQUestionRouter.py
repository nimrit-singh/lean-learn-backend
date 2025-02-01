from fastapi import APIRouter, status
from services.FillQuestionService import get_all_fill_questions,Create_fill_question,get_one_fill_question,update_fill_question,delete_fill_question
from schemas.fillQuestionsSchema import FillQuestionSchema as fillSchema

router = APIRouter(
    prefix="/fillquestion",
    tags=["fillquestions"]
)

@router.get("/" ,status_code=status.HTTP_200_OK, response_model=list[fillSchema])
def get_all():
    return get_all_fill_questions()

@router.get("/{id}" ,status_code=status.HTTP_200_OK)
def get_one(id: str):
    return get_one_fill_question(id)

@router.post("/" ,status_code=status.HTTP_200_OK)
def create_fill_question(fillSchema: fillSchema):
    return Create_fill_question(fillSchema)

@router.put("/{id}" ,status_code=status.HTTP_200_OK)
def update_one(id: str, fillSchema: fillSchema):
    return update_fill_question(id, fillSchema) 

@router.delete("/{id}" ,status_code=status.HTTP_200_OK)
def delete_one(id: str):
    return delete_fill_question(id) 
    