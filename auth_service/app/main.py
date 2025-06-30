from fastapi import FastAPI
import uvicorn

from config import settings
from api import v1_router

app = FastAPI()
app.include_router(v1_router, prefix=settings.api.prefix)

if __name__ == '__main__':
    uvicorn.run(
        app=settings.run.app,
        host=settings.run.host,
        port=settings.run.port,
        # reload=settings.run.reload,
        reload=True
    )