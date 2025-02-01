from models.FormulaQuestionsEntity import formula_question_entity , formula_question_entitys
from schemas.formulsSchema import FormulsSchema
from database.database import formula_collection
from fastapi import status , HTTPException 
from bson import ObjectId

def get_all_formula_questions():
    items = formula_collection.find()
    return formula_question_entitys(items)

def get_one_formula_question(id: str):
    item = formula_collection.find_one({"_id": ObjectId(id)})
    return formula_question_entity(item)

def Create_formula_question(formulaSchema: FormulsSchema):
    question = formula_collection.find_one({"question": formulaSchema.question})
    if question:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Question already exists")
    
    question_dict = formulaSchema.model_dump()
    insterted_item = formula_collection.insert_one(question_dict)
    question_dict["_id"] = insterted_item.inserted_id
    return formula_question_entity(question_dict)

def update_formula_question(id: str, formulaSchema: FormulsSchema):
    item = formula_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    question_dict = formulaSchema.model_dump()
    question_dict["_id"] = ObjectId(id)
    formula_collection.update_one({"_id": ObjectId(id)}, {"$set": question_dict})
    return formula_question_entity(question_dict)

def delete_formula_question(id: str):   
    item = formula_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    formula_collection.delete_one({"_id": ObjectId(id)})
    return formula_question_entity(item)

