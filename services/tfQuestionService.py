from models.tfQuestionEntity import tfEntity , tfEntitys
from schemas.tfSchema import tfSchema
from database.database import tf_collection
from fastapi import status , HTTPException
from bson import ObjectId


def get_all_tf_questions():
    items = tf_collection.find()
    if items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return tfEntitys(items) 


def Create_tf_question(tfSchema: tfSchema):
    question = tf_collection.find_one({"question": tfSchema.question})
    if question:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Question already exists")
    
    question_dict = tfSchema.model_dump()
    insterted_item = tf_collection.insert_one(question_dict)
    question_dict["_id"] = insterted_item.inserted_id
    return tfEntity(question_dict)  


def get_one_tf_question(id: str):
    item = tf_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return tfEntity(item)


def update_tf_question(id: str, tfSchema: tfSchema):
    item = tf_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    question_dict = tfSchema.model_dump()
    question_dict["_id"] = ObjectId(id)
    tf_collection.update_one({"_id": ObjectId(id)}, {"$set": question_dict})
    return tfEntity(question_dict)


def delete_tf_question(id: str):
    item = tf_collection.find_one({"_id": ObjectId(id)})
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    tf_collection.delete_one({"_id": ObjectId(id)})
    return tfEntity(item)  

    