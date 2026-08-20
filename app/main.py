from fastapi import FastAPI

from app.config import APPLICATION_NAME
from app.routes.health import router

app = FastAPI(title=APPLICATION_NAME)

app.include_router(router)
