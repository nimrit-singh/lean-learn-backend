from database.database import mcq_collection
from fastapi import status , HTTPException
from models.mcqQuestionEntity import mcqEntity , mcqEntitys
from schemas.mcqSchema import mcqSchema
from bson import ObjectId

def get_all_mcq_questions():
    items = mcq_collection.find()
    if items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return mcqEntitys(items)

def Create_mcq_question(mcqSchema: mcqSchema):
    question = mcq_collection.find_one({"question": mcqSchema.question})
    if question:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Question already exists")
    
    question_dict = mcqSchema.model_dump()
    insterted_item = mcq_collection.insert_one(question_dict)
    question_dict["_id"] = insterted_item.inserted_id
    return mcqEntity(question_dict)

def get_one_mcq_question(id: str):
    item = mcq_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return mcqEntity(item)


def update_mcq_question(id: str, mcqSchema: mcqSchema):
    item = mcq_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    question_dict = mcqSchema.model_dump()
    question_dict["_id"] = ObjectId(id)
    mcq_collection.update_one({"_id": ObjectId(id)}, {"$set": question_dict})
    return mcqEntity(question_dict)

def delete_mcq_question(id: str):
    item = mcq_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    mcq_collection.delete_one({"_id": ObjectId(id)})
    return mcqEntity(item)