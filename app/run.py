import uvicorn
from fastapi import FastAPI # need python-multipart
from app.views import router

app = FastAPI(title="AdviNow Interview Challenge", version="1.6")
app.include_router(router)
