from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import word, feedback, summary

app = FastAPI(title="Worddee.ai API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(word.router)
app.include_router(feedback.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Worddee.ai Backend up and running"}

    