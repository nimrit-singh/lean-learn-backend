from pydantic import BaseModel
from typing import List

class WrongAnswerSchema(BaseModel):
    question: str
    topic: str
    answer: str
    choosen_answer: str
    
class ReportSchema(BaseModel):
    total_question: int
    correct_question: List[str]
    incorrect_question: List[str]
    accuracy: float
    topics: List[str]
    wrong_answers: List[WrongAnswerSchema]    