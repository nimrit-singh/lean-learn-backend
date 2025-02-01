from models.fillQuestionsEntity import fillquestionEntity , fillquestionEntitys
from schemas.fillQuestionsSchema import FillQuestionSchema
from database.database import fill_collection
from fastapi import status , HTTPException
from bson import ObjectId


def get_all_fill_questions():
    items = fill_collection.find()
    if items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return fillquestionEntitys(items)


def get_one_fill_question(id: str):
    item = fill_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return fillquestionEntity(item) 


def Create_fill_question(fillSchema: FillQuestionSchema):
    question = fill_collection.find_one({"question": fillSchema.question})
    if question:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Question already exists")
    
    question_dict = fillSchema.model_dump()
    insterted_item = fill_collection.insert_one(question_dict)
    question_dict["_id"] = insterted_item.inserted_id
    return fillquestionEntity(question_dict)


def update_fill_question(id: str, fillSchema: FillQuestionSchema):
    item = fill_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    question_dict = fillSchema.model_dump()
    question_dict["_id"] = ObjectId(id)
    fill_collection.update_one({"_id": ObjectId(id)}, {"$set": question_dict})
    return fillquestionEntity(question_dict)


def delete_fill_question(id: str):  
    item = fill_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    fill_collection.delete_one({"_id": ObjectId(id)})
    return fillquestionEntity(item)