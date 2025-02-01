from fastapi import APIRouter, status
from services.tfQuestionService import get_all_tf_questions,Create_tf_question,get_one_tf_question,update_tf_question,delete_tf_question
from schemas.tfSchema import tfSchema

router = APIRouter(
    prefix="/tfquestion",
    tags=["tfquestions"]
)   

@router.get("/" ,status_code=status.HTTP_200_OK, response_model=list[tfSchema])
def get_all():
    return get_all_tf_questions()

@router.post("/" ,status_code=status.HTTP_200_OK)
def create_tf_question(tfSchema: tfSchema):
    return Create_tf_question(tfSchema) 

@router.get("/{id}" ,status_code=status.HTTP_200_OK)
def get_one(id: str):
    return get_one_tf_question(id)  

@router.put("/{id}" ,status_code=status.HTTP_200_OK)
def update_one(id: str, tfSchema: tfSchema):
    return update_tf_question(id, tfSchema)

@router.delete("/{id}" ,status_code=status.HTTP_200_OK)
def delete_one(id: str):
    return delete_tf_question(id)