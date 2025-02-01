from fastapi import APIRouter, status
from services.formulaQuestionService import get_all_formula_questions,Create_formula_question,get_one_formula_question,update_formula_question,delete_formula_question
from schemas.formulsSchema import FormulsSchema as formulaSchema



router = APIRouter(
    prefix="/formula",
    tags=["formulaquestions"]
)

@router.get("/" ,status_code=status.HTTP_200_OK, response_model=list[formulaSchema])
def get_all():
    return get_all_formula_questions()

@router.get("/{id}" ,status_code=status.HTTP_200_OK , response_model=formulaSchema)
def get_one(id: str):
    return get_one_formula_question(id)


@router.post("/" ,status_code=status.HTTP_200_OK , response_model=formulaSchema)
def create_formula_question(formulaSchema: formulaSchema):
    return Create_formula_question(formulaSchema)

@router.put("/{id}" ,status_code=status.HTTP_200_OK , response_model=formulaSchema)
def update_one(id: str, formulaSchema: formulaSchema):
    return update_formula_question(id, formulaSchema)

@router.delete("/{id}" ,status_code=status.HTTP_200_OK , response_model=formulaSchema)
def delete_one(id: str):
    return delete_formula_question(id)
