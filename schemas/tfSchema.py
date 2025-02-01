from pydantic import BaseModel

class tfSchema(BaseModel):
    id: str
    class_: str
    subject: str
    topic: str
    question: str
    answer: str
    resource: str
    used: bool
