from pydantic import BaseModel
from typing import List

class QuantitySchema(BaseModel):
    name: str
    symbol: str
    isUnknown: bool
class FormulaSchema(BaseModel):
    name: str
    symbol: str
class FormulsSchema(BaseModel):
    id: str
    class_: str
    subject: str
    topic: str
    question: str
    quantities: List[QuantitySchema]
    formula: List[FormulaSchema]
    options: List[str]  # Empty array as it's not used for formula questions
    answers: List[str]  # Empty array as it's not used for formula questions
    resource: List[str]  # Empty array as per the API requirement
    used: bool