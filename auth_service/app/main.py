from fastapi import FastAPI
import uvicorn

from config import settings
from routes import v1_users_router

app = FastAPI()
app.include_router(v1_users_router, prefix=settings.api.prefix)


if __name__ == '__main__':
    uvicorn.run(
        app=settings.run.app,
        host=settings.run.host,
        port=settings.run.port,
        reload=(settings.run.reload, True),
    )