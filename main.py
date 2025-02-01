from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from api.mcqQuestionRouter import router as mcq_router
from api.tfQuestionRouter import router as tf_router
from api.aiRouter import router as ai_router
from api.formulaQuestionRouter import router as formula_router
from api.fillQUestionRouter import router as fill_router
import uvicorn
app = FastAPI()
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )
origins = [
    "http://localhost:5173",
    "https://leanlearn01.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow all headers
)
app.include_router(tf_router)
app.include_router(mcq_router)
app.include_router(fill_router)
app.include_router(formula_router)
app.include_router(ai_router)