from ai.gemini_llm import generate_details
from ai.openAI_llm import create_explaination
from schemas.aiSchema import WrongAnswerSchema

def get_explaination(wrongAnswer):
    return create_explaination(wrongAnswer)

def get_report(question: str):
    return generate_details(question)