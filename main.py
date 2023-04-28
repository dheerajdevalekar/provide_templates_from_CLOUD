from fastapi import FastAPI
from uvicorn import run
from loguru import logger
from db.models import init_db
from src.routes.all_routes import router


title = f"Get Templates from Cloud V1.0"
project_port = 35400

app = FastAPI(title="Get Templates from Cloud \n V1.0")

app.include_router(router)


@app.on_event("startup")
async def init_processes():
    try:
        print(init_db())
    except Exception as e:
        logger.critical(f"Init Process Error: {e}")


if __name__ == '__main__':
    logger.info(f"Started Code {title} with Port: {project_port}")
    run("main:app", host="0.0.0.0", port=project_port, reload=True)
