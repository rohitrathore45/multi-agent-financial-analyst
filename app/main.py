from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.getcwd(), "app", ".env"))

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Financial Analyst API",
    description="Multi-Agent AI + ML Financial System",
    version="1.0"
)

app.include_router(router)