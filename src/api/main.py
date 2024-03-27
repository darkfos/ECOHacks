from fastapi import FastAPI
from src.api.routers import v1_router

import uvicorn

app: FastAPI = FastAPI(title="EcoAPI")


#include routers
app.include_router(v1_router)


def run_fast_app() -> None:
    """
    Run application
    """

    uvicorn.run(app=app)
