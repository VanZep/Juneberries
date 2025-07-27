from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from config import settings
from models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Функция старта и завершения работы приложения."""
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    title=settings.app.title,
    summary=settings.app.summary,
    description=settings.app.description
)

if __name__ == '__main__':
    uvicorn.run(
        app=settings.run.app,
        host=settings.run.host,
        port=settings.run.port,
        reload=(settings.run.reload, True),
    )